# BioProject: Genomic Scanner & Analyzer 🧬

BioProject es una herramienta profesional de bioinformática diseñada para el escaneo, identificación y análisis funcional de secuencias de ADN. Combina la potencia del motor local **NCBI BLAST+** con la conectividad global de la **API de NCBI (QBlast)**.

## 🚀 Funcionalidades Principales

### 1. Escaneo Local
Permite realizar búsquedas ultra-rápidas contra una base de datos propia almacenada en la carpeta `database/`. Ideal para identificar secuencias previamente conocidas o variantes locales sin necesidad de internet. Utiliza índices optimizados (`.nhr`, `.nin`, `.nsq`).

### 2. Escaneo Global (NCBI Worldwide)
Conecta directamente con los servidores de NCBI en Maryland, USA, para comparar una secuencia contra la base de datos **nt** (nucleótidos), la más grande del mundo. Identifica organismos, patógenos y genes con precisión científica (E-value).

### 3. Laboratorio de Análisis Funcional
Más allá de la búsqueda, este módulo interpreta la secuencia:
- **Traducción a Proteína**: Simula el dogma central de la biología convirtiendo ADN en una cadena de Aminoácidos hasta encontrar un codón de parada.
- **Contenido GC**: Calcula la estabilidad termodinámica de la secuencia, útil para identificar firmas genómicas.

### 4. Historial Inteligente (JSON)
Todas las búsquedas y hallazgos se registran automáticamente en un archivo `history.json`, permitiendo auditoría científica y persistencia de datos para futuros análisis.

## 🛠️ Estructura del Proyecto

- `main.py`: Punto de entrada con menú interactivo.
- `bio_project/core/`: Motores de búsqueda y lógica de análisis.
- `bio_project/cli/`: Interfaces de línea de comandos.
- `bio_project/database/`: Almacén de archivos FASTA.
- `bio_project/logs/`: Historial de consultas en formato JSON.

## 📦 Instalación

1. **Requisitos**: Tener instalado [NCBI BLAST+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download).
2. **Entorno**:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install biopython
   ```
3. **Ejecución**:
   ```powershell
   python main.py
   ```

## 🚀 Futuras Mejoras (Roadmap)

Este proyecto es una base sólida que puede expandirse en las siguientes direcciones:

1.  **Integración de Scraping Automático**: Crear un módulo que extraiga automáticamente las últimas secuencias de variantes de interés (E.g., nuevas cepas de virus) desde repositorios públicos como GISAID o NCBI Virus.
2.  **Visualización Filogenética**: Implementar la generación de árboles filogenéticos (`Phylo` de Biopython) para visualizar la distancia evolutiva entre los resultados encontrados.
3.  **Detección de Mutaciones Específicas**: Añadir un comparador que resalte cambios puntuales (SNPs) entre la secuencia query y el "Top Hit" de la base de datos.
4.  **Predicción de Estructura 3D**: Integrar enlaces o scripts para conectar las secuencias de proteínas traducidas con herramientas de predicción de plegamiento (como mini-implementaciones inspiradas en AlphaFold).
5.  **Interfaz Web (Dashboard)**: Migrar la CLI actual a un dashboard interactivo utilizando **Streamlit** o **Flask** para visualizar resultados con gráficos de barras y mapas de calor genómicos.
6.  **Soporte Multihilo**: Optimizar las búsquedas locales masivas utilizando procesamiento en paralelo para grandes archivos FASTA.

---
*Desarrollado para ingeniería bioinformática y análisis genómico.*
