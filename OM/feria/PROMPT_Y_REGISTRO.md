# PROMPT Y REGISTRO DE ACTIVIDADES

**Fecha:** 22/10/2026 (cuarta sesión)  
**Modelo/herramienta:** opencode con Nemotron 3 Ultra (nvidia/nemotron-3-ultra-550b-a55b)  
**Carpeta de trabajo:** /home/camiloasd/Documentos/VS/Trabajos-de-Investigacion-Redaccion/OM/feria

## Prompt original
(Este archivo contiene el prompt completo proporcionado por el usuario al inicio de la sesión)

## Resumen de actividades realizadas en esta sesión

### 0. Confirmación de ubicación
Todos los archivos están en la misma carpeta (feria/): main.tex, portada.tex, referencias.bib, tabla_unica_RSL.xlsx, tabla_unica_RSL_cribada.xlsx, tabla_unica_RSL_cribada_v2.xlsx, tabla_unica_RSL_cribada_v3.xlsx, tabla_unica_RSL_cribada_v4.xlsx, scielo.csv, scopus_86.csv, reporte_deduplicacion.md, merge_dedup.py, CAMBIOS.md, PROMPT_Y_REGISTRO.md, respaldo/, respaldo_2/, respaldo_3/, respaldo_4/, respaldo_5/, respaldo_6/

### 1. Backup en respaldo_6/
Copiados: main.tex, referencias.bib → respaldo_6/

### 2. Referencias (referencias.bib regenerado - 85 entradas)
- **Volumen, número, páginas/articleno** añadidos desde CSVs originales (scopus_86.csv, scielo.csv) para TODAS las entradas. 0 entradas incompletas.
- **Títulos en formato oración (APA 7)**: función `to_sentence_case()` que pone mayúscula solo la primera palabra y protege siglas (GLOF, HEC-RAS, IBER, FEA, AI, ML, HPC, MW, PGA, etc.) y nombres propios (Perú, Lima, Callao, Chile, Colombia, etc.) con llaves en el .bib.
- **Revistas sin sufijo de país**: eliminados "(Switzerland)" de Water, Sustainability, Geosciences, etc. via `clean_journal()`.
- **URLs limpias**: eliminados puntos finales, `fix_url()`.
- **Autores**: parseo mejorado para "Van den Bosch, F. J." etc.
- **DOI**: mantenidos donde existen; comentario "% DOI no disponible en la exportación" donde no.
- **SciELO DOIs**: verificados en páginas de artículos; ninguno de los 16 registros SciELO incluidos/dudosos tiene DOI en la exportación CSV ni en la página web (todos usan URL de scielo.org). 16 DOIs no comprobables.
- **"y" vs "&"**: biblatex-apa con `language=spanish` y `DeclareLanguageMapping{spanish}{spanish-apa}` usa "y" automáticamente en citas y bibliografía. Configuración correcta.

### 3. Categorías normalizadas en xlsx v4 (hoja "Categorías")
- **Técnica (9 categorías, 69 incluidos)**: Modelado hidrodinámico/hidráulico 24 (34.8%), Modelado deslizamientos/GLOF 13 (18.8%), Simulación numérica tsunami 12 (17.4%), Inversión formas de onda 7 (10.1%), Modelos atenuación (GMM) 7 (10.1%), Gemelos digitales/Fotogrametría 4 (5.8%), Teledetección/Análisis geoespacial 3 (4.3%), ML físico-informado/IA híbrida 2 (2.9%), HPC/Computación paralela 1 (1.4%).
- **Desastre (9 categorías, 69 incluidos)**: Inundación fluvial 17 (24.6%), Tsunami 15 (21.7%), Sismo 14 (20.3%), Deslizamiento 9 (13.0%), GLOF 3 (4.3%), Inundación costera 3 (4.3%), Flujo de escombros 2 (2.9%), Capacitación 1 (1.4%), Sequía 1 (1.4%).

### 4. main.tex actualizado
- **RQ1**: párrafo con conteos por técnica y desastre normalizados (sin mencionar "columna" ni "archivo"). Párrafo único nombrando los 6 registros de inversión de formas de onda/modelación fuentes sísmicas y tsunamis con cita al final.
- **RQ3**: 5 citas separadas, cada una junto a su afirmación:
  * `garcia2025parallel` → TUNAMI-N2 en Tohoku University
  * `escobarsilva2023assessing, flores2026numerical` → HEC-RAS
  * `lengonzlez2022curso` → curso cubano formación docente
  * `varelaledesma2021tecnolog` → tecnología gestión sequía para toma decisiones

### 5. Compilación
`latexmk -pdf main` → **EXITOSO** (main.pdf 12 páginas, 0 errores, 0 citas indefinidas, sin advertencias evitables de LaTeX/biber). Cifras en texto, tablas y xlsx coinciden.

### 6. Registros actualizados
CAMBIOS.md y PROMPT_Y_REGISTRO.md

## Entrega breve

### Qué corregí
1. Referencias: 85 entradas con vol/num/páginas desde CSVs, títulos APA 7, revistas sin país, URLs limpias.
2. xlsx v4: hoja "Categorías" con 9 técnicas y 9 desastres normalizados + conteos/porcentajes.
3. main.tex: RQ1 con análisis por técnica normalizada; RQ3 con citas separadas por afirmación; párrafo único de 6 registros sísmicos.
4. Compilación limpia (0 errores, 0 undefined citations).

### Quedó pendiente
- Verificación manual de DOIs de SciELO (16 registros sin DOI en exportación ni web).
- Comprobar que los 6 registros de inversión de formas de onda citados en RQ1 coincidan exactamente con los del xlsx.

### ACTIVIDADES MANUALES PENDIENTES (mínimo)
1. **Revisar los 16 "dudoso"** (13 Scopus + 3 SciELO) y la **propuesta de 14 artículos** para lectura a texto completo — confirmar/modificar decisiones.
2. **Descargar y leer a texto completo** los 10-15 artículos elegidos (priorizar: tsunami Perú, GLOF, inundaciones Andes, ML físico-informado, estudios SciELO con Iber/HEC-RAS).
3. **Verificar cada dato y cita** contra su fuente (DOI, autores, año, revista, hallazgos, vol/num/pág).
4. **Elegir imagen del background** (máx. 2 págs) y añadir fuente/cita en Figura 1.
5. **Escribir resumen definitivo** (≥250 palabras, sin citas), **introducción** (8 párrafos) y **conclusiones** (respuesta sintética RQ1–RQ3 + recomendaciones).
6. **Poner tu nombre y fecha** en portada.tex.
7. **Confirmar con docente**: autoría individual, declaración de uso de IA, y si interlineado 1.5 aplica también a referencias.
8. **Completar celdas pendientes** en tabla de flujo (texto completo, síntesis final) y hoja Extracción.
9. **Revisar referencias.bib**: confirmar vol/num/páginas, corregir campos si hay errores.
10. **Crear "Anexo metodológico"** (documento suplementario) con la justificación caso por caso de los 10 registros límite.
