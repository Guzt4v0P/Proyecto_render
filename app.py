import pandas as pd
import plotly.express as px
import streamlit as st


df = pd.read_csv('vehicles_us.csv')

bar_button = st.button('Gáfica de barras')
if bar_button:
    st.write('Creación de un gráfico de barras de la condición de los vehículos')
    fig = px.bar(df, x="condition", title="Distribución de la Condición de los Vehículos")
    st.plotly_chart(fig, use_container_width=True)

line_button = st.button('Gráfica lineal')
if line_button:
    st.write('Creación de grafica lineal de días listados por año del modelo ')
    fig = px.line(df.groupby('model_year')['days_listed'].mean().reset_index(),
                  x='model_year', y='days_listed', title="Días Listados por Año del Modelo")
    st.plotly_chart(fig, use_container_width=True)


dispersion_button = st.button('Gráfica de dispersión de precio-odómetro')
if dispersion_button:
    st.write('Gráfico de dispersión Precio vs. Odómetro')
    fig = px.scatter(df, x="odometer", y="price", 
                     title="Precio vs. Odómetro",
                     labels={'odometer': 'Kilometraje (millas)', 'price': 'Precio (USD)'})
    st.plotly_chart(fig, use_container_width=True)





