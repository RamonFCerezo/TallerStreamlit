import streamlit as st
import pandas as pd
import numpy as np

def display():
    c1, c2 = st.columns([9,1])
    c1.title("Algunos widgets de Streamlit")

    st.divider()
    with st.echo("below"):
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.button("Mi botón")
        show_code = c2.checkbox("Ver código")
        c3.number_input("Input de número", value=5, min_value=0, max_value=10, step=1)
        c4.text_input("Input de texto")
        c5.metric("Visualizaciones", "3203493")
    
    st.markdown("---")
    with st.echo("below"):
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.slider("Slider numérico", value=50, min_value=0, max_value=100, step=1)
        c2.select_slider("Slider de Texto", options=["ultrabook", "notebook", "gaming", "2-in-1"])
        c3.radio("CPU", options=["Intel", "AMD"])
        c4.selectbox("Sistema Operativo", options=["Chrome OS", "Windows 10", "Windows 7"])
        c5.multiselect("Marca", options=["Asus", "Lenovo", "Dell", "Toshiba", "HP", "LG"]) 