import streamlit as st
from PIL import Image
from rembg import remove

def display():
    st.header('Quitamos el fondo a una imagen')
    st.markdown('En primer lugar, le pedimos al usuario que suba la imagen a la que debemos quitar el fondo')
    uploaded_file = st.file_uploader("Cargar fotografía .jpg", type=["jpg"])
    # Subir un archivo jpg desde la computadora
    if uploaded_file != None:
        input = Image.open(uploaded_file)
        output = remove(input)
        st.image(output)
