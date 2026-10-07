"""Funciones para cargar y revisar el dataset weatherAUS."""

from pathlib import Path

import pandas as pd

COLUMNAS_ESPERADAS = [
    "Date", "Location", "MinTemp", "MaxTemp", "Rainfall", "Evaporation",
    "Sunshine", "WindGustDir", "WindGustSpeed", "WindDir9am", "WindDir3pm",
    "WindSpeed9am", "WindSpeed3pm", "Humidity9am", "Humidity3pm",
    "Pressure9am", "Pressure3pm", "Cloud9am", "Cloud3pm", "Temp9am",
    "Temp3pm", "RainToday", "RainTomorrow",
]


def raiz_proyecto():
    """Busca la carpeta del proyecto (la que tiene README.md y data/)."""
    ruta = Path.cwd().resolve()
    for carpeta in [ruta, *ruta.parents]:
        if (carpeta / "README.md").exists() and (carpeta / "data").exists():
            return carpeta
    raise FileNotFoundError("No se encontro la carpeta del proyecto.")


def cargar_weather(ruta=None):
    """Carga weatherAUS.csv desde data/raw con ruta relativa."""
    if ruta is None:
        ruta = raiz_proyecto() / "data" / "raw" / "weatherAUS.csv"
    ruta = Path(ruta)
    if not ruta.exists():
        raise FileNotFoundError(
            f"No se encontro {ruta}. Descarga el CSV desde Kaggle y dejalo en data/raw/"
        )
    datos = pd.read_csv(ruta, parse_dates=["Date"], na_values=["NA"])
    return datos


def validar_columnas(datos):
    """Revisa que esten las 23 columnas del dataset original."""
    faltantes = [c for c in COLUMNAS_ESPERADAS if c not in datos.columns]
    if faltantes:
        raise ValueError(f"Faltan columnas: {faltantes}")
    return True


def resumen_nulos(datos):
    """Tabla con cantidad y porcentaje de nulos por columna."""
    tabla = pd.DataFrame({
        "nulos": datos.isnull().sum(),
        "porcentaje": (datos.isnull().mean() * 100).round(2),
    })
    return tabla.sort_values("porcentaje", ascending=False)
