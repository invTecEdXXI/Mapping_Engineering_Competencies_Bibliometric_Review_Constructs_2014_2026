# Leiden-Inspired Indicators Report

> NOTA: Indicadores normalizados intra-corpus. NO usar para comparaciones inter-institucionales formales. La normalizacion de campo se basa en conceptos OpenAlex nivel 0.

## MNCS (Mean Normalized Citation Score)
- Corpus mean MNCS: 0.927 (n=96, incluye articulos con 0 citas)
- Articles above field mean (MNCS > 1): 19/96

### By Field
> Nota metodologica: el promedio de MNCS *dentro de cada campo* es matematicamente ~1.0 por construccion (cada articulo ya esta normalizado por la media de su propio campo), asi que esta tabla NO sirve para comparar campos entre si -- solo informa el N de articulos y si el campo tuvo 0 citas en conjunto (media=0.0).

- **Psychology**: mean MNCS=1.0, n=54
- **Computer science**: mean MNCS=1.0, n=22
- **Engineering**: mean MNCS=1.0, n=11
- **Unknown**: mean MNCS=0.0, n=6
- **Sociology**: mean MNCS=1.0, n=2
- **Philosophy**: mean MNCS=0.0, n=1

## PP(top 10%): 0.094
- Total in top 10%: 9/96

## MNJS (Mean Normalized Journal Score)
- Mean MNJS: 1.0
- Articles with SJR data: 51/96

## Bias Detection
- Ningun umbral de sesgo (idioma/geografico/cobertura) se disparo.