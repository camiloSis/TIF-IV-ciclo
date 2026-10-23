# Reporte de deduplicación — RSL Física computacional y gestión del riesgo de desastres

**Fecha de procesamiento:** 22/10/2026
**Herramienta:** script de Python (`merge_dedup.py`), ejecutado por Claude (Sonnet 5.5) sobre los CSV exportados.

## Fuentes

| Base | Exportación | Query | Registros |
|---|---|---|---|
| Scopus | 22/10/2026, 14:50 | `TITLE-ABS-KEY ( ( "numerical simulation" OR "numerical model" OR "numerical modeling" OR "computational model" OR "hydrodynamic model" OR "physics-informed" OR "high-performance computing" ) AND ( "disaster risk" OR flood OR floods OR landslide OR earthquake OR "early warning" ) AND ( peru OR "latin america" OR andean OR "south america" ) ) AND PUBYEAR > 2020 AND DOCTYPE ( ar OR re )` | 86 |
| SciELO | 22/10/2026, 18:24 | `(simulación OR modelación OR "modelo numérico" OR "modelo hidrodinámico" OR "modelo hidráulico") AND (desastres OR inundaciones OR sismos OR deslizamientos OR "gestión del riesgo")` (con filtros de idioma, año y colección) | 34 |

## Criterios de deduplicación (en este orden)

1. DOI idéntico (normalizado). Los registros de SciELO no traen DOI en la exportación, por lo que solo aplica a Scopus.
2. Título idéntico tras normalizar (minúsculas, sin tildes ni signos).
3. Título similar con razón de coincidencia ≥ 0,90 (se revisa como posible duplicado).

## Resultado

- Registros antes de deduplicar: **120** (86 Scopus + 34 SciELO)
- Duplicados eliminados: **0**
- Registros únicos: **120**

Verificación adicional: la mayor similitud entre un título de SciELO y uno de Scopus fue 0,49, muy lejos del umbral. No hay solapamiento entre las dos bases.

## Observaciones para el cribado

- 1 registro de Scopus tiene año **2027** (publicación anticipada): queda fuera del rango 2021–2026.
- 1 registro de Scopus no tiene DOI; en SciELO ninguno lo trae (se usa el enlace).
- Los 34 registros de SciELO no incluyen resumen en la exportación: hay que leerlos en la página del artículo.
- Varios registros de SciELO parecen fuera de tema (por ejemplo, simulación de ejercicio y función cardiopulmonar, riesgo financiero minero, salas de análisis de salud pública por COVID-19). Se descartarán en el cribado por título y resumen.
- Ningún registro de SciELO proviene de la colección de Perú.
