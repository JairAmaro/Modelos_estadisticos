import numpy as np
import pandas as pd

# Autor: Equipo 3

def generar_dataframe():
    """ Función para generar un DataFrame con 100 filas y las siguientes columnas:
    - U1: 100 valores aleatorios entre 0 y 1 (por la indicacion de que sea uniforme (0,1))
    - U2: 100 valores aleatorios entre 0 y 1
    - V1: 2 * U1 - 1
    - V2: 2 * U2 - 2
    - S: raíz cuadrada de V1^2 + V2^2
    - Decision: 1 si S > 1, 0 en otro caso
    - x: 0 si S <= 0, V1 * sqrt(-2 * log(S) / S) en otro caso
    - y: 0 si S <= 0, V2 * sqrt(-2 * log(S) / S) en otro caso
    
    Parametros:
        None
    Returns:
        pd.DataFrame: DataFrame con las columnas 'U1', 'U2', 'V1', 'V2', 'S', 'Decision', 'x', 'y'
    """

    U1 = np.random.uniform(0, 1, 100)
    U2 = np.random.uniform(0, 1, 100)
    
    V1 = 2 * U1 - 1
    V2 = 2 * U2 - 2
    
    S = np.sqrt(V1**2 + V2**2)
    
    Decision = np.where(S > 1, 1, 0)
    
    # Evitar valores invalidos en logaritmo y división para la desicion ya que cuando sea 0 los tomara como NaN
    valid_mask = (S > 0) & (S <= 1)
    
    x = np.zeros_like(S)
    y = np.zeros_like(S)
    
    x[valid_mask] = V1[valid_mask] * np.sqrt(-2 * np.log(S[valid_mask]) / S[valid_mask])
    y[valid_mask] = V2[valid_mask] * np.sqrt(-2 * np.log(S[valid_mask]) / S[valid_mask])
    
    df = pd.DataFrame({
        'U1': U1,
        'U2': U2,
        'V1': V1,
        'V2': V2,
        'S': S,
        'Decision': Decision,
        'x': x,
        'y': y
    })
    
    return df

# Generar y mostrar el DataFrame
df = generar_dataframe()
df.to_excel("C:/Users/oscar/Downloads/Practica_12.xlsx", index=False)