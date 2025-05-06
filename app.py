import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de anuncios de vehículos.')

# Checkbox para histograma
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Histograma para la columna odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión (odómetro vs precio)'):
    st.write('Gráfico de dispersión entre odómetro y precio')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)
