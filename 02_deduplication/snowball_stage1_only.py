"""Corre SOLO Stage 1 (terminologico, sin LLM) del cribado real de
screeningMejorar sobre los 3,408 candidatos de snowballing de Cadena A.

Objetivo: justificar de forma trazable por que NO se completa el cribado
semantico (Stage 2, con costo de API) sobre los candidatos de snowballing --
si Stage 1 (deterministico, gratis) ya descarta la abrumadora mayoria por no
mencionar el bloque conceptual de poblacion/contexto ("engineering student*"
etc.), eso es evidencia documentable de que el rendimiento esperado de
completar el cribado no justifica el costo.

Reusa el MISMO codigo del pipeline real (generate_screening_criteria +
terminological_screening + export_stage1_csv) -- no es una reimplementacion
paralela, es exactamente lo que correria main.py en Fase 0a.

Uso: python snowball_stage1_only.py (correr desde screeningMejorar/ o con
screeningMejorar en el PYTHONPATH -- ver sys.path.insert abajo)
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

SCREENING_MEJORAR = Path(__file__).resolve().parents[2] / "screeningMejorar"
sys.path.insert(0, str(SCREENING_MEJORAR))

import os
os.chdir(SCREENING_MEJORAR)  # config.py resuelve rutas relativas a CWD

from src.data_loader import load_consolidado
from src.screening_criteria import generate_screening_criteria
from src.terminological_screener import terminological_screening
from src.screening_export import export_stage1_csv
from src.llm_client import LLMClient

CAD_A_DIR = Path(__file__).resolve().parent
CONTRACT_COLUMNS = ["key", "Author", "Title", "Year", "Abstract", "Keywords", "Author_Keywords"]


def make_key(author: str, year: str, used: Counter) -> str:
    surname = "Unknown"
    if author:
        first_author = author.split(";")[0].strip()
        surname = re.sub(r"[^A-Za-z]", "", first_author.split(",")[0]) or "Unknown"
    base = f"{surname}{year or 'sf'}"
    n = used[base]
    used[base] += 1
    return base if n == 0 else f"{base}{chr(ord('a') + n - 1)}"


def build_contract_csv(src_path: Path, dst_path: Path) -> int:
    with open(src_path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter=";"))

    used: Counter = Counter()
    out_rows = []
    for r in rows:
        key = make_key(r.get("Author", ""), r.get("Year", ""), used)
        out_rows.append({
            "key": key,
            "Author": r.get("Author", ""),
            "Title": r.get("Title", ""),
            "Year": r.get("Year", ""),
            "Abstract": r.get("Abstract", ""),
            "Keywords": "",
            "Author_Keywords": "",
        })

    with open(dst_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CONTRACT_COLUMNS, delimiter=";", quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(out_rows)
    return len(out_rows)


def main():
    src_csv = CAD_A_DIR / "snowball_candidatos_cadA.csv"
    contract_csv = CAD_A_DIR / "snowball_candidatos_cadA_contrato.csv"

    n = build_contract_csv(src_csv, contract_csv)
    print(f"Adaptados {n} candidatos al contrato -> {contract_csv.name}")

    articles = load_consolidado(str(contract_csv))
    print(f"Cargados por data_loader (con abstract valido >=50 chars): {len(articles)}")

    # OJO: articulo2B/propuestaCadA.txt (raiz) esta DESACTUALIZADO (aun dice
    # "2015"); la copia real usada para correr el cribado, con el fix a 2014,
    # es la de screeningMejorar/ -- usar esa, no la de la raiz.
    proposal_path = str(SCREENING_MEJORAR / "propuestaCadA.txt")
    proposal_text = Path(proposal_path).read_text(encoding="utf-8")
    print(f"Protocolo: {proposal_path} ({len(proposal_text)} chars)")

    llm = LLMClient(provider="deepseek")  # no se invoca red: protocolo v2 texto no usa LLM aqui

    criteria = generate_screening_criteria(
        proposal_text, llm, session_id="snowballCadA",
        use_cache=False, review_type="systematic",
        proposal_path=proposal_path,
    )
    if not criteria.get("phase_1_terminological"):
        print("ERROR: no se pudieron generar criterios Stage 1 desde el protocolo.")
        return

    results = terminological_screening(articles, criteria)

    n_included = len(results.get("included", []))
    n_excluded = len(results.get("excluded", []))
    print(f"\nStage 1 resultado: {n_included} pasan a Stage 2 (hipoteticamente) / {n_excluded} excluidos automaticamente")
    print(f"Tasa de descarte por Stage 1: {n_excluded / (n_included + n_excluded) * 100:.1f}%")

    # Motivos de exclusion mas comunes
    reasons = Counter(d.get("automatic_exclusion_reason", "?") for d in results.get("excluded", []))
    print("\nMotivos de exclusion:")
    for reason, count in reasons.most_common():
        print(f"  {reason}: {count}")

    missing_block_counter = Counter()
    for d in results.get("excluded", []):
        for mb in d.get("missing_blocks", []):
            missing_block_counter[mb] += 1
    print("\nBloques conceptuales ausentes (entre los excluidos por vacio_conceptual):")
    for block, count in missing_block_counter.most_common():
        print(f"  {block}: {count}")

    out_path = export_stage1_csv(articles, results, session_id="snowballCadA", output_dir=CAD_A_DIR)
    print(f"\nCSV trazable exportado: {out_path}")


if __name__ == "__main__":
    main()
