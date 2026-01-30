import streamlit as st
import pandas as pd

def exibir_lista(df: pd.DataFrame, top: int):
    st.subheader("🏆 Ranking do Mês")

    df = df.head(top)

    for _, row in df.iterrows():
         st.markdown(
            f"""
            <div class="card">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div class="rank">{row['rank']}°</div>
                    <div class="title">{row['titulo']}</div>
                </div>
                <div class="artist">{row['artista']}</div>
                <div style="margin-top: 8px;">
                    <a href="{row['spotify_url']}" target="_blank">
                        Ouvir no Spotify
                    </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.write("Fonte: [Billboard Hot 100](https://www.billboard.com/charts/hot-100)")
