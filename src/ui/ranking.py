import streamlit as st
import pandas as pd

def exibir_top3(df: pd.DataFrame):
    podium = [df.iloc[1], df.iloc[0], df.iloc[2]]
    podium_df = pd.DataFrame(podium).reset_index(drop=True)

    medals = ["🥈", "🥇", "🥉"]

    cards = ""

    for i, row in podium_df.iterrows():
        cards += f"""
        <div class="top-card {'center' if i == 1 else ('left' if i == 0 else 'right')}">
            <div class="rank-badge">{medals[i]}</div>
            <img src="{row['image']}" />
            <div class="title">{row['titulo']}</div>
            <div class="artist">{row['artista']}</div>
            <a href="{row['spotify_url']}" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174872.png" 
                    alt="Spotify Logo" 
                    style="width: 30px; height: 30px;"/>
            </a>
        </div>
        """

    st.markdown(
        f"""
        <h3 style="text-align:center;">🏆 Top 3</h3>
        <div class="top3-container">
            {cards}
        </div>
        """,
        unsafe_allow_html=True
    )

def exibir_ranking_completo(df: pd.DataFrame, top: int):
    st.subheader("Ranking Completo")

    for i, row in df.head(top).iloc[3:].iterrows():
        st.markdown(
            f"""
            <div class="rank-row">
                <div class="rank-number">{row['rank']}</div>
                <img src="{row['image']}" />
                <div class="rank-info">
                    <div class="title">{row['titulo']}</div>
                    <div class="artist">{row['artista']}</div>
                </div>
                <a href="{row['spotify_url']}" target="_blank"> 
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174872.png" 
                    alt="Spotify Logo" 
                    style="width: 25px; height: 25px;"/>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
