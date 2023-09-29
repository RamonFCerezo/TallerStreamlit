import streamlit as st

def display():
    st.title('Más widgets')
    st.markdown("---")
    with st.echo("below"):
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.download_button("Descargar archivo", data=b"0101", help="Una explicación al botón")
        c2.file_uploader("Cargar archivos")
        c3.color_picker("Seleccionar color")
        c4.date_input("Seleccionar fecha")  
        c5.time_input("Seleccionar hora")  

    st.markdown("---")
    with st.echo("below"):
        c1, c2, c3, c4 = st.columns(4)
        c1.error("Mensaje de error")
        c2.warning("Mensaje de warning")
        c3.info("Mensaje informativo")
        c4.success("Mensaje de éxito")