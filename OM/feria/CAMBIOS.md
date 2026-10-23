# CAMBIOS POR ARCHIVO (Sesión 4 - 22/10/2026)

## main.tex
### Modificado:
1. **RQ1: Análisis preliminar** (sección 3.3.1):
   - Reescrito con categorías normalizadas de técnica (9 categorías) y tipo de desastre (9 categorías), con conteos y porcentajes sobre 69 incluidos.
   - Eliminada mención a "columna Tipo de desastre" y "archivo de datos".
   - Añadido párrafo único nombrando los 6 registros de inversión de formas de onda/modelación de fuentes sísmicas y tsunamis con cita al final.
   - Mantenidos párrafos de HPC, ML físico-informado, teledetección, y nota sobre SciELO sin resumen.

2. **RQ3: Análisis preliminar** (sección 3.3.3):
   - Separadas las 5 citas para que cada una quede junto a la afirmación que respalda:
     * `garcia2025parallel` → TUNAMI-N2 en Tohoku University
     * `escobarsilva2023assessing, flores2026numerical` → HEC-RAS
     * `lengonzlez2022curso` → curso cubano formación docente
     * `varelaledesma2021tecnolog` → tecnología gestión sequía para toma decisiones

3. **Compilación**: `latexmk -pdf main` → **EXITOSO** (12 páginas, 0 errores, 0 citas indefinidas, sin advertencias evitables).

## referencias.bib
### Regenerado totalmente (85 entradas):
1. **Volumen, número, páginas/articleno** añadidos desde CSVs originales (Scopus y SciELO) para todas las entradas.
2. **Títulos en formato oración (APA 7)**: primera palabra mayúscula, resto minúsculas salvo siglas (GLOF, HEC-RAS, IBER, FEA, AI, ML, HPC, etc.) y nombres propios (Perú, Lima, Callao, Chile, Colombia, etc.) protegidos con llaves en el .bib.
3. **Revistas sin sufijo de país**: eliminados "(Switzerland)" de Water, Sustainability, Geosciences, etc.
3. **URLs limpias**: eliminados puntos finales, espaciado corregido.
4. **Autores**: parseo mejorado para "Van den Bosch, F. J." etc.
5. **DOI**: mantenidos donde existen; comentario "% DOI no disponible" donde no.
6. **Comillas "y" vs "&"**: biblatex-apa con `language=spanish` usa "y" automáticamente (configuración correcta).

## tabla_unica_RSL_cribada_v4.xlsx
### Actualizado:
1. **Columna 17 "Técnica de física computacional"**: categorías consolidadas (9 categorías) para los 69 incluidos.
2. **Hoja "Categorías"**: dos tablas con conteos y porcentajes:
   - Desastre: Inundación fluvial 17 (24.6%), Tsunami 15 (21.7%), Sismo 14 (20.3%), Deslizamiento 9 (13.0%), GLOF 3 (4.3%), Inundación costera 3 (4.3%), Flujo de escombros 2 (2.9%), Capacitación 1 (1.4%), Sequía 1 (1.4%).
   - Técnica: Modelado hidrodinámico/hidráulico 24 (34.8%), Modelado deslizamientos/GLOF 13 (18.8%), Simulación numérica tsunami 12 (17.4%), Inversión formas de onda 7 (10.1%), Modelos atenuación (GMM) 7 (10.1%), Gemelos digitales/Fotogrametría 4 (5.8%), Teledetección/Análisis geoespacial 3 (4.3%), ML físico-informado/IA híbrida 2 (2.9%), HPC/Computación paralela 1 (1.4%).
3. **Hoja "Propuesta lectura"**: 14 principales + 5 suplentes (sin cambios).
4. **Hoja "Verificación citas"**: 63 entradas (sin cambios).

## Compilación
- `latexmk -pdf main` → **EXITOSO** (main.pdf 12 páginas, 0 errores, 0 citas indefinidas, 0 advertencias evitables).
- Cifras en texto, tablas y xlsx coinciden (69 incluidos, 9 categorías técnica, 9 categorías desastre).

## Archivos de registro
- CAMBIOS.md y PROMPT_Y_REGISTRO.md actualizados con esta sesión.
