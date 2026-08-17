import streamlit as st
import pandas as pd

st.set_page_config(page_title="Control de Gastos", layout="wide")

st.title("Control de Gastos Personales")

st.write("Aplicación inicial para registrar ingresos, gastos y bancos.")

datos = pd.DataFrame({
    "Tipo": ["Ingreso", "Gasto", "Gasto"],
    "Descripción": ["Salario", "Comida", "Transporte"],
    "Monto": [1500, 250, 100]
})

st.subheader("Movimientos de prueba")
st.dataframe(datos)

total_ingresos = datos[datos["Tipo"] == "Ingreso"]["Monto"].sum()
total_gastos = datos[datos["Tipo"] == "Gasto"]["Monto"].sum()
saldo = total_ingresos - total_gastos

col1, col2, col3 = st.columns(3)

col1.metric("Ingresos", f"L {total_ingresos:,.2f}")
col2.metric("Gastos", f"L {total_gastos:,.2f}")
col3.metric("Saldo", f"L {saldo:,.2f}")
