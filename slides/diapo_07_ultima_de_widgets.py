import streamlit as st

def display():
    st.title('Y aún unos poquitos más')
    st.markdown("---")
    with st.echo("below"):
        c1, c2, c3, c4 = st.columns(4)
        if c1.button("¡Bravo!"):
            st.balloons()
        if c2.button("Progreso"):
            import time
            my_bar = c2.progress(0)
            for i in range(0,101,10):
                my_bar.progress(i)
                time.sleep(.2)
            my_bar.empty()
        if c3.button("Mensaje dinámico"):
            import time
            with st.spinner('Desaparecerá en 1.5 segundos...'):
                time.sleep(1.5)
        if c4.button("Mensaje de Excepción"):
            try:
                1/0
            except Exception as e:
                st.exception(e)