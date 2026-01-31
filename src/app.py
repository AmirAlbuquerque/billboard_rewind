import streamlit as st
from datetime import date
from service.billboard_service import carregar_hot100

from config.page_config import configurar_layout
from ui.layout import render_sidebar
from ui.ranking import exibir_top3, exibir_ranking_completo

# Configuração global
configurar_layout()

# Conteúdo principal
st.title("Billboard Rewind")
st.write("Ranking das músicas mais populares dos EUA")

# Estado inicial
hoje = date.today()
if 'df_atual' not in st.session_state:
    with st.spinner("Carregando ranking do mês atual..."):
        st.session_state.df_atual = carregar_hot100(hoje.year, hoje.month)

# Renderiza a barra lateral e obtém os filtros
ano, mes, top_n, buscar = render_sidebar()

# Ação do usuário
if buscar:
    with st.spinner("Buscando ranking selecionado..."):
        st.session_state.df_atual = carregar_hot100(ano, mes)

# Exibição
if st.session_state.df_atual.empty:
    st.warning("⚠️ Não há dados disponíveis para este mês.")
else:
    exibir_top3(st.session_state.df_atual)
    exibir_ranking_completo(st.session_state.df_atual, top_n)
st.write("Fonte: [Billboard Hot 100](https://www.billboard.com/charts/hot-100)")