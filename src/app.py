import streamlit as st
from datetime import date
from database import carregar_hot100

from config.page_config import apply_dark_theme
from ui.layout import setup_page, render_sidebar
from ui.ranking_view import exibir_lista

# Configuração global
setup_page()
apply_dark_theme()

# Conteúdo principal
st.title("🎶 Billboard Hot 100")
st.write("Ranking das músicas mais populares do mundo")

# Estado inicial
hoje = date.today()
if 'df_atual' not in st.session_state:
    with st.spinner("🔄 Carregando ranking do mês atual..."):
        st.session_state.df_atual = carregar_hot100(hoje.year, hoje.month)

# Renderiza a barra lateral e obtém os filtros
ano, mes, top_n, buscar = render_sidebar()

# Ação do usuário
if buscar:
    with st.spinner("🔄 Buscando ranking selecionado..."):
        st.session_state.df_atual = carregar_hot100(ano, mes)

# Exibição
exibir_lista(st.session_state.df_atual, top_n)