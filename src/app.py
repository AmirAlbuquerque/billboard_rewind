import streamlit as st

from config.page_config import apply_dark_theme
from ui.layout import setup_page, render_sidebar

# Configuração global
setup_page()
apply_dark_theme()

# Conteúdo principal
st.title("🎶 Billboard Hot 100")
st.write("Ranking das músicas mais populares do mundo")

# Renderiza a barra lateral e obtém os filtros
ano, mes, top_n, buscar = render_sidebar()