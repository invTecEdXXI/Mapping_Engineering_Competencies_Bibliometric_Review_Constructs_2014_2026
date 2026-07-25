"""Snowballing (backward + forward citation search) via OpenAlex API.

PRISMA 2020: "Records identified via other methods" (citation searching),
distinto de la busqueda en las 6 bases de datos ya hecha. Parte de los 92
articulos ya incluidos en Cadena A:
  - Backward: que citan ellos (sus referencias)
  - Forward: quien los cita a ellos despues (mas relevante para encontrar
    estudios NUEVOS que se hayan publicado tras la busqueda original)

Filtra automaticamente lo que ya esta en el corpus de 906 (por DOI y por
titulo fuzzy) y lo que cae fuera del rango de anio del protocolo (2014-2026).
NO decide inclusion -- eso lo hace screeningMejorar con propuestaCadA.txt
despues, igual que con el resto del corpus. Esto solo genera candidatos.

Salida: snowball_candidatos_cadA.csv (contrato similar al de screeningMejorar
+ columnas de procedencia: origen, desde_articulos, venue/ISSN/DOAJ para
verificar indexacion).

Uso: python snowball_openalex.py
"""
from __future__ import annotations

import csv
import os
import re
import time
from difflib import SequenceMatcher
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / "screeningMejorar" / ".env")

OPENALEX_BASE = "https://api.openalex.org"
MAILTO = os.getenv("OPENALEX_EMAIL", "")  # polite pool
API_KEY = os.getenv("OPENALEX_API_KEY", "")  # $1/dia gratis vs $0.10/dia sin key
YEAR_MIN, YEAR_MAX = 2014, 2026


def normalize_title(t: str) -> str:
    t = (t or "").lower()
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def title_similar(a: str, b: str, threshold: float = 0.90) -> bool:
    return SequenceMatcher(None, a, b).ratio() >= threshold


def openalex_get(url: str, params: dict | None = None):
    params = dict(params or {})
    if MAILTO:
        params["mailto"] = MAILTO
    if API_KEY:
        params["api_key"] = API_KEY
    for attempt in range(3):
        try:
            resp = requests.get(url, params=params, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            if resp.status_code == 429:
                print(f"    [429] {resp.text[:150]}")
                time.sleep(5)
                continue
            print(f"    [HTTP {resp.status_code}] {resp.text[:150]}")
        except requests.RequestException as e:
            print(f"    [request error] {e}")
        time.sleep(2 * (attempt + 1))
    return None


def resolve_work(doi: str, title: str):
    if doi:
        clean_doi = doi.replace("https://doi.org/", "").strip()
        data = openalex_get(f"{OPENALEX_BASE}/works/doi:{clean_doi}")
        if data and "id" in data:
            return data
    data = openalex_get(f"{OPENALEX_BASE}/works", {"search": title, "per_page": 1})
    if data and data.get("results"):
        return data["results"][0]
    return None


def batch_fetch_works(openalex_ids: list[str]):
    results = []
    ids = [i.rsplit("/", 1)[-1] for i in openalex_ids]
    for i in range(0, len(ids), 50):
        chunk = ids[i : i + 50]
        filt = "openalex_id:" + "|".join(chunk)
        data = openalex_get(f"{OPENALEX_BASE}/works", {"filter": filt, "per_page": 50})
        if data:
            results.extend(data.get("results", []))
        time.sleep(0.15)
    return results


def get_citing_works(openalex_id: str, cap: int = 200):
    short_id = openalex_id.rsplit("/", 1)[-1]
    data = openalex_get(
        f"{OPENALEX_BASE}/works",
        {"filter": f"cites:{short_id}", "per_page": min(cap, 200)},
    )
    if not data:
        return []
    return data.get("results", [])


def reconstruct_abstract(inv_idx: dict | None) -> str:
    if not inv_idx:
        return ""
    pos_word = {}
    for word, positions in inv_idx.items():
        for p in positions:
            pos_word[p] = word
    return " ".join(pos_word[i] for i in sorted(pos_word))


def work_to_row(work: dict) -> dict:
    doi = (work.get("doi") or "").replace("https://doi.org/", "")
    title = work.get("title") or work.get("display_name") or ""
    authors = "; ".join(
        a["author"]["display_name"] for a in work.get("authorships", []) if a.get("author")
    )
    venue = (work.get("primary_location") or {}).get("source") or {}
    return {
        "openalex_id": work.get("id", ""),
        "doi": doi,
        "Title": title,
        "Year": work.get("publication_year", ""),
        "Author": authors,
        "Abstract": reconstruct_abstract(work.get("abstract_inverted_index")),
        "venue": venue.get("display_name", "") if venue else "",
        "venue_issn": ",".join((venue.get("issn") or [])) if venue else "",
        "is_in_doaj": venue.get("is_in_doaj", "") if venue else "",
        "cited_by_count": work.get("cited_by_count", 0),
    }


def load_corpus_index(path: str):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter=";"))
    dois = {(r.get("DOI") or "").strip().lower().replace("https://doi.org/", "") for r in rows}
    dois.discard("")
    titles = {normalize_title(r.get("Title", "")) for r in rows}
    return dois, titles, {r["Key"]: r for r in rows}


def main():
    corpus_dois, corpus_titles, merged_rows = load_corpus_index("consolidado_merged.csv")

    with open("cadenaAIncluidos.csv", encoding="utf-8-sig", newline="") as f:
        included = list(csv.DictReader(f, delimiter=";"))

    candidates: dict[str, dict] = {}
    backward_from: dict[str, set] = {}
    forward_from: dict[str, set] = {}
    unresolved = []

    for i, art in enumerate(included, 1):
        key = art["key"]
        title = art["Title"]
        src = merged_rows.get(key, {})
        doi = (src.get("DOI") or "").strip()
        print(f"[{i}/{len(included)}] {key} (doi={'si' if doi else 'no'}) ...")

        work = resolve_work(doi, title)
        if not work:
            unresolved.append(key)
            print("  NO resuelto en OpenAlex")
            continue

        ref_ids = work.get("referenced_works", [])
        if ref_ids:
            for w in batch_fetch_works(ref_ids):
                row = work_to_row(w)
                oid = row["openalex_id"]
                candidates.setdefault(oid, row)
                backward_from.setdefault(oid, set()).add(key)

        for w in get_citing_works(work["id"]):
            row = work_to_row(w)
            oid = row["openalex_id"]
            candidates.setdefault(oid, row)
            forward_from.setdefault(oid, set()).add(key)

        time.sleep(0.1)

    print(f"\nNo resueltos en OpenAlex: {len(unresolved)} -> {unresolved}")
    print(f"Candidatos brutos (backward+forward, deduplicados): {len(candidates)}")

    new_candidates = []
    for oid, row in candidates.items():
        doi_l = row["doi"].lower()
        if doi_l and doi_l in corpus_dois:
            continue
        norm_t = normalize_title(row["Title"])
        if not norm_t:
            continue
        if any(title_similar(norm_t, ct) for ct in corpus_titles):
            continue
        try:
            year = int(row["Year"])
        except (ValueError, TypeError):
            year = None
        if year is not None and not (YEAR_MIN <= year <= YEAR_MAX):
            continue

        b = oid in backward_from
        fw = oid in forward_from
        row["origen"] = "backward+forward" if (b and fw) else ("backward" if b else "forward")
        row["desde_articulos"] = "; ".join(
            sorted(backward_from.get(oid, set()) | forward_from.get(oid, set()))
        )
        new_candidates.append(row)

    print(f"Candidatos nuevos (fuera del corpus de 906, anio {YEAR_MIN}-{YEAR_MAX}): {len(new_candidates)}")

    new_candidates.sort(key=lambda r: -(r.get("cited_by_count") or 0))

    out_cols = [
        "origen", "desde_articulos", "doi", "Title", "Year", "Author",
        "venue", "venue_issn", "is_in_doaj", "cited_by_count", "Abstract",
    ]
    with open("snowball_candidatos_cadA.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=out_cols, delimiter=";", quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for row in new_candidates:
            writer.writerow({k: row.get(k, "") for k in out_cols})

    print("Escrito snowball_candidatos_cadA.csv")


if __name__ == "__main__":
    main()
