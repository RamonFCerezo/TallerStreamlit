import streamlit as st
import glob
import importlib

def display():
    # Crear pestañas
    titulos_pestanas = ['Qué es Streamlit', 'Para qué podemos usar Streamlit', 'Código Pestañas']
    pestañas = st.tabs(titulos_pestanas)
    
    # Contenido de cada pestaña
    with pestañas[0]:
        st.header('Qué es Streamlit')
        st.markdown('- Es una biblioteca basada en Python')
        st.markdown('- Se complementa con otras bibliotecas que ya conocemos')
        st.markdown('- Nos permite crear WebApps sin saber HTML o CSS, como sucede con Flask, y otros frameworks')
        st.markdown("- <p style='color:green'>Os he mentido un poco, sí se pueden poner HTML o CSS, como en este caso, para darle color a nuestro texto, pero no es necesario</p>", unsafe_allow_html=True)
    
    with pestañas[1]:
        st.header('Para qué podemos usar Streamlit')
        st.write('')
        st.markdown('- Para compartir modelos con personas que no saben Python')
        st.markdown('- Para exponer un EDA con gráficos interactivos')
        st.markdown('- Para crear aplicaciones web con diferentes utilidades: edición de fotos, juegos, obtención de datos')

    with pestañas[2]:
        st.header('Y así de fácil se hace la estructura de pestañas')
        st.code("""titulos_pestanas = ['Qué es Streamlit', 'Para qué podemos usar Streamlit', 'Código Pestañas']
pestañas = st.tabs(titulos_pestanas)
# Para llenar cada pestaña de contenido:
with pestañas[0]:
    st.header('Qué es Streamlit')
    # Resto del contenido 
with pestañas[1]:
    # Contenido
with pestañas[2]:
    # Contenido""")