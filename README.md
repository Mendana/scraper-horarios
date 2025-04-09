# 📅 Scrapper y Formateador de csv para la BBDD de horarios del PCEO (Informática + Matemáticas)

Este proyecto automatiza por completo el scraping, procesamiento y unificación de los horarios de asignaturas del Grado en Ingeniería Informática y las asignaturas de Matemáticas (SharePoint), en un único CSV bien formateado listo cargarlas en la BBDD

---

## 🚀 ¿Qué hace?

- 📥 Scrapea los horarios desde:
  - El portal de la Escuela de Ingeniería Informática
  - Un repositorio en SharePoint con los horarios de Matemáticas
- 📄 Descarga los CSV y los convierte al formato final:
    ```
    Day,Start,End,Subject,Room
    
    10/09/2024,09:00,10:00,ALG.T.1,A-2-01
    ....
    ```
- 🧹 Limpia carpetas temporales
- ✅ Todo se ejecuta con un solo comando: `py main.py`

---

## 🛠️ Tecnologías utilizadas

- **Python 3.10+**
- [`pandas`](https://pandas.pydata.org/) – manipulación de CSVs
- [`playwright`](https://playwright.dev/python/) – automatización del scraping
- `glob`, `shutil`, `os` – gestión de archivos/carpetas
- `datetime` – formateo de fechas y horas

---

## 📦 Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/Mendana/scraper-horarios.git
cd scraper-horarios
```
### 2. Crear y activar entorno virtual
- En Windows:
    ```bash
    python -m venv env
    env\Scripts\activate
    ```
- En macOS/Linux
    ```bash
    python -m venv env
    source env/bin/activate
    ```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
playwright install  # para instalar los navegadores
```
> 💡 `Nota`: playwright install es necesario solo la primera vez.

---

## ▶️ Ejecución

Una vez todo instalado, simplemente hay que ejecutar:
```bash
python main.py
```
Esto va a ejecutar automáticamente:
1. `InforScrapper.py` – scraping del portal de informática
2. `MathScrapper.py` – scraping de horarios desde SharePoint
3. `joinCSV.py` – unir horarios individuales de informática
4. `InforFormatter.py` – transformar horarios de informática al formato final
5. `MathFormatter.py` – transformar horarios de matemáticas al formato final
6. `theBoss.py` – unir ambos resultados en horario_final_completo.csv
7. Limpieza automática de carpetas dataI/ y dataM/

---

## 🗂️ Estructura del repositorio

```
scraper-horarios/
├── dataI/                    ← CSVs temporales de informática
├── dataM/                    ← CSVs temporales de mates
├── InforScrapper.py          ← Scraper para el portal de informática
├── MathScrapper.py           ← Scraper para SharePoint de mates
├── joinCSV.py                ← Une CSVs individuales de informática
├── InforFormatter.py         ← Da formato final al CSV de informática
├── MathFormatter.py          ← Da formato final al CSV de mates
├── theBoss.py                ← Une ambos finales en uno solo
├── main.py                   ← 🔥 Ejecuta todo el pipeline
├── requirements.txt          ← Dependencias del proyecto
```

---

## ✅ Resultado final

Al ejecutar el script principal, obtendrás:
``` bash
horario_final_completo.csv
```

---

## 👤 Autor
Desarrollado por Diego Díaz Mendaña – para automatizar la descarga y generación del csv de todas las asignaturas para la BBDD
