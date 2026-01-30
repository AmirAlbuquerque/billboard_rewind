import streamlit as st
import pandas as pd

def exibir_lista(df: pd.DataFrame, top: int):
    st.subheader("🏆 Ranking do Mês")

    df = df.head(top)

    for _, row in df.iterrows():
        st.markdown(
            f"""
            **#{row['rank']}** 🎵 **{row['titulo']}**  
            *{row['artista']}*
            👉 [Ouvir no Spotify 🎧]({row['spotify_url']}
            ---
            """
        )
    st.write("Fonte: [Billboard Hot 100](https://www.billboard.com/charts/hot-100)")
