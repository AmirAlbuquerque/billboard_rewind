import streamlit as st

def apply_dark_theme():
    st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
