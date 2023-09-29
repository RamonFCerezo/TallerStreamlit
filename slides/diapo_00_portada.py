import streamlit as st
import glob
import importlib
import random
import pandas as pd

def display():
    st.header("""Streamlit: la WebApp que te hará la vida fácil""")
    st.divider()
    c1, c2 = st.columns([.5,.5])
    c1.image('images/giphy.gif', use_column_width="auto")
    codigo = c2.checkbox("Ver código")
    if codigo:
        c2.code(body = """st.header('Streamlit: la WebApp que 
te hará la vida fácil')
st.divider()
c1, c2 = st.columns([.5,.5])
c1.image('images/giphy.gif', width=350)
codigo = c2.checkbox("Ver código") 
if codigo:
    c2.code(body =""")
