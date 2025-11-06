import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Vehicles EDA App")

@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    return df

df = load_data()

st.write("### Tabela de dados (primeiras linhas)")
st.write(df.head())

st.write(f"**Total de linhas:** {df.shape[0]}")
st.write(f"**Total de colunas:** {df.shape[1]}")

# Histograma
if st.button("Mostrar Histograma - Odometer"):
    fig = px.histogram(df, x="odometer", title="Histograma do Odometer")
    st.plotly_chart(fig, use_container_width=True)

# Scatter Price vs Model Year
if st.button("Mostrar Scatter - Price vs Model Year"):
    fig = px.scatter(df, x="model_year", y="price",
                     title="Preço vs Ano do Modelo (model_year)")
    st.plotly_chart(fig, use_container_width=True)