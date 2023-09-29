import streamlit as st
import glob
import importlib
import re


# Configurar la página de la aplicación
st.set_page_config(page_title="Taller Streamlit", page_icon="images/Streamlit-icon.png", layout="wide")

c1, c2 = st.columns([.85, .20])
c1.title('Taller Streamlit')
c1.caption('Ramón Fernández Cerezo')
c2.image('images/Streamlit-logo.png', width=200)

STARTING_SLIDE = 0
slide_files = sorted(glob.glob("slides/diapo_*.py"))
N = len(slide_files)

if 'slide_number' not in st.session_state:
	st.session_state.slide_number = STARTING_SLIDE

# Upper menu

c1, c2, c3 = st.sidebar.columns([.5, .4, .5])
c1.write("")
c1.write("")
if c1.button("Anterior") and st.session_state.slide_number>0:
    st.session_state.slide_number -= 1
c3.write("")
c3.write("")
if c3.button("Siguiente") and st.session_state.slide_number<N-1:
    st.session_state.slide_number += 1
slide = c2.text_input("Diapositiva:", value=f"{st.session_state.slide_number}")
st.session_state.slide_number = int(slide)

# Display the slides
module_str = re.sub(r"\\", ".", slide_files[st.session_state.slide_number])
# module_str = module_str.replace(".py","")
module_str = module_str + '.py'
current_slide = importlib.import_module(module_str)
current_slide.display()