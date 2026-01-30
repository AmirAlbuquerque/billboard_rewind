import streamlit as st
from datetime import date

def setup_page():
    st.set_page_config(
        page_title="🎶 Billboard Hot 100",
        page_icon="🎧",
        layout="centered",
        initial_sidebar_state="expanded"
    )

def render_sidebar():
    st.sidebar.header("📅 Filtros")

    hoje = date.today()

    ano = st.sidebar.selectbox(
        "Ano",
        list(range(1980, hoje.year + 1)),
        index=(hoje.year - 1980)
    )

    mes = st.sidebar.selectbox(
        "Mês",
        list(range(1, 13)),
        index=(hoje.month - 1)
    )

    top_n = st.sidebar.number_input(
        "Quantidade do TOP",
        min_value=1,
        max_value=100,
        value=10,
        step=1
    )

    buscar = st.sidebar.button("🎯 Buscar ranking")

    return ano, mes, top_n, buscar