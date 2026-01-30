import streamlit as st

def apply_dark_theme():
    st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    a {
        text-decoration: none;
        color: #1DB954; /* Spotify green */
        font-weight: 600;
    }

    a:hover {
        text-decoration: underline;
    }

    .card {
        background-color: #161b22;
        padding: 16px 20px;
        border-radius: 12px;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    .rank {
        font-size: 22px;
        font-weight: 700;
    }
    .title {
        font-size: 18px;
        font-weight: 600;
    }
    .artist {
        font-size: 15px;
        color: #b3b3b3;
    }
    
    </style>
    """, unsafe_allow_html=True)
