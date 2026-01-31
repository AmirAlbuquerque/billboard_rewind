import streamlit as st
from datetime import date

def render_sidebar():
    st.sidebar.header("📅 Filtros")

    hoje = date.today()

    ano = st.sidebar.selectbox(
        "Ano",
        list(range(1980, hoje.year + 1))[::-1],
        index=0
    )

    mes = st.sidebar.selectbox(
        "Mês",
        list(range(1, 13)),
        index=0
    )

    top_n = st.sidebar.number_input(
        "Quantidade do TOP",
        min_value=1,
        max_value=100,
        value=10,
        step=1
    )

    buscar = st.sidebar.button("Buscar")

    return ano, mes, top_n, buscar