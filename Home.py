import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title='Huntsville MBB Performance Analysis',
                   layout="wide", 
                   page_icon="whitelogo.png",
                   initial_sidebar_state="expanded")
col1, col2 = st.columns([6, 1])
with col1:
    st.title("Huntsville HS MBB Performace Analysis")
    st.header('2024-2025')
    st.markdown("""
    <style>
    .big-font {font-size:13px !important;}
</style>
""", unsafe_allow_html=True)
    
st.markdown('<p class="big-font">Developed by Huntsville High School MBB Director of Scouting and Analytics: Coach Cole Davis</p>', unsafe_allow_html=True)

with col2:
    st.image("whitelogo.png", width=175)
st.markdown("___")
###################################################

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("How to understand and use advanced stats")

excel_file1 = 'analytics_database.xlsx'
sheet_name1 = 'homepagedata'
sheet_name2 = 'homepagedata2'

df1 = pd.read_excel(excel_file1,
                   sheet_name=sheet_name2,
                   usecols='A:B',
                   header=1)
df2 = pd.read_excel(excel_file1,
                    sheet_name=sheet_name1,
                    usecols='A:Q',
                    header=1)

with col1:
    st.dataframe(df1, hide_index=True)
    st.subheader("Advanced Stats Season Averages")
    st.dataframe(df2, hide_index=True)

