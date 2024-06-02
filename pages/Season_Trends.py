import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Huntsville MBB Performance Analysis',
                   layout="wide", 
                   page_icon="whitelogo.png",
                   )
col1, col2 = st.columns([6, 1])
with col1:
    st.title("Season Trends")
    st.markdown("""
    <style>
    .big-font {font-size:13px !important;}
</style>
""", unsafe_allow_html=True)
    
    st.markdown('<p class="big-font">Analyze player trends throughout the season</p>', unsafe_allow_html=True)

with col2:
    st.image("whitelogo.png", width=120)
st.markdown("___")

#################################