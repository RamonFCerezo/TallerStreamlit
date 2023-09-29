import streamlit as st
import pandas as pd
import numpy as np

def display():
    df = pd.read_csv('data\\train.csv')
    data = {'jornada': range(1,39),
    'posición': [1, 5, 8, 12, 15, 19, 16, 20, 18, 14, 11, 7, 4, 2, 6, 10, 13,
                 17, 20, 16, 12, 9, 5, 3, 7, 11, 14, 18, 20, 17, 13, 10, 6, 4,
                 8, 12, 15, 19]}
    df = pd.DataFrame(data)

    st.data_editor(
    df,
    column_config={
    "posición": st.column_config.ProgressColumn(
    "posición",
    help="Posición en liga",
    format="%f",
    min_value=0,
    max_value=20)},hide_index=True)
    codigo = st.checkbox("Ver código")
    if codigo:
        st.code(body = """df = pd.read_csv('data\\train.csv')
        st.data_editor(
        df,
        column_config={
        "posicion": st.column_config.ProgressColumn(
        "posicion",
        help="Size of the TVS",
        format="%f",
        min_value=10,
        max_value=20)},hide_index=True)""")
    st.line_chart(df['posición'])