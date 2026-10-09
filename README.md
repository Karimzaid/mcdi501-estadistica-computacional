# mcdi501-estadistica-computacional

Repositorio del curso MCDI501 Estadística Computacional (Magíster en Ciencia de Datos e IA, UNAB).

**Grupo 4**

- Jeremmy Díaz Alfaro
- Karim Zaid Sánchez
- Laura Arenas Kosin

## Dataset

Usamos el dataset **Rain in Australia** (`weatherAUS.csv`) de Kaggle:
https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package

- Tiene observaciones diarias del clima en varias ciudades de Australia.
- Son 23 columnas (temperatura, lluvia, viento, humedad, presión, nubes, etc.).
- La variable `RainTomorrow` indica si llovió al día siguiente (Yes/No).
- El archivo original está en `data/raw/` y no se modifica. Lo que se procese se guarda en `data/processed/`.

## Estructura

```
mcdi501-estadistica-computacional/
├── data/
│   ├── raw/            # datos originales (weatherAUS.csv)
│   └── processed/      # datos procesados
├── notebooks/
│   └── 01_formativa1_eda.ipynb   # carga, estadística descriptiva y figuras
├── figuras/            # figuras que genera el notebook
├── src/
│   └── carga_datos.py  # funciones para cargar y revisar los datos
├── requirements.txt
└── README.md
```

## Cómo ejecutar

```bash
python -m venv .venv
.venv\Scripts\activate        # en Windows
python -m pip install -r requirements.txt
python -m jupyterlab
```

Después abrir `notebooks/01_formativa1_eda.ipynb` y ejecutar todo (Restart & Run All).
Las rutas son relativas, así que funciona en cualquier computador que clone el repo.
