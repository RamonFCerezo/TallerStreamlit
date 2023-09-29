import streamlit as st
import glob
import importlib
import pandas as pd

def display():
    st.header("Ejemplo de cómo insertar DataFrame y mostrarlo por pantalla")
 
    # Subir un archivo CSV desde la computadora
    uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])

    if uploaded_file is not None:
        # Leer el archivo CSV y crear un DataFrame
        df = pd.read_csv(uploaded_file)

        # Mostrar el DataFrame en Streamlit
        st.write('DataFrame desde archivo CSV:')
        st.dataframe(df)