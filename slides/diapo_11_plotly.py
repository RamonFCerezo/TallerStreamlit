import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

def display():
    # Título de la aplicación
    st.title("Gráfico de Líneas y Gráfico Circular con Plotly en Streamlit")

    # Datos para el gráfico de líneas
    datos_lineas = {
        "x": ["Singapur", 'Bahrein', 'Monza', 'Imola', 'Miami', 'México'],
        "y": [14, 3, 8, 4, 5, 1]
    }

    # Crear el gráfico de líneas
    plt.title('Posiciones de Alonso F1 2023')
    figura_lineas = px.line(datos_lineas, x="x", y="y", title="Gráfico de Líneas")

    # Mostrar el gráfico de líneas en la WebApp
    st.plotly_chart(figura_lineas)

    # Datos ficticios para el pie chart
    datos_pie = {
        "labels": ["Red Bull", "Mercedes", "Ferrari", "Aston Martin", "McLaren"],
        "values": [640, 300, 280, 200, 190]
    }

    # Crear el pie chart
    figura_pie = px.pie(datos_pie, names="labels", values="values", title="Gráfico Circular")
    st.plotly_chart(figura_pie)
