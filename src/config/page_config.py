import streamlit as st

def apply_dark_theme():
    st.markdown("""
    <style>
    .top3-container {
        display: flex;
        justify-content: center;
        gap: 24px;
        margin-top: 24px;
        padding-bottom: 40px;
    }

    .top-card {
        background: white;
        color: #0f172a;
        border-radius: 16px;
        padding: 20px;
        width: 240px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    }
                
    .top-card img {
        width: 160px;
        height: 160px;
        border-radius: 12px;
        object-fit: cover;
        margin-bottom: 12px;
    }

    .rank-badge {
        font-size: 22px;
        margin-bottom: 8px;
    }

    .title {
        font-weight: 700;
        font-size: 16px;
        color: #020617;
    }

    .artist {
        color: #475569;
        font-size: 14px;
        margin-bottom: 12px;
    }

    .rank-list {
        margin-top: 32px;
    }

    .rank-row {
        display: flex;
        align-items: center;
        background: white;
        color: #0f172a;
        padding: 12px 16px;
        border-radius: 12px;
        margin-bottom: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    .rank-number {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        background: #f1f5f9;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        margin-right: 12px;
    }

    .rank-row img {
        width: 48px;
        height: 48px;
        border-radius: 8px;
        margin-right: 12px;
    }

    .rank-info {
        flex: 1;
    }

    .rank-info .title {
        font-size: 15px;
    }

    .rank-info .artist {
        font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)
