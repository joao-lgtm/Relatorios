import pandas as pd
import numpy as np

def traduzTipoColunas(df: pd.DataFrame):
    tipos_simplificados = {}
    for coluna, tipo in df.dtypes.items():
        if pd.api.types.is_string_dtype(tipo):
            tipos_simplificados[coluna] = "string"
        elif pd.api.types.is_numeric_dtype(tipo):
            tipos_simplificados[coluna] = "number"
        elif pd.api.types.is_datetime64_any_dtype(tipo):
            tipos_simplificados[coluna] = "date"
        elif pd.api.types.is_bool_dtype(tipo):
            tipos_simplificados[coluna] = "boolean"
        else:
            tipos_simplificados[coluna] = str(tipo)
    return tipos_simplificados
