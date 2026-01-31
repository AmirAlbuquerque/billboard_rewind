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

def exibir_top3(df: pd.DataFrame):
    top1 = df.iloc[0]
    top2 = df.iloc[1]
    top3 = df.iloc[2]
    # top3 = df.head(3)
    podium = [top2, top1, top3]
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
