import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

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
    .big-font {font-size:15px !important;}
</style>
""", unsafe_allow_html=True)
    
st.markdown('<p class="big-font">Developed by Huntsville High School MBB Director of Scouting and Analytics: Coach Cole Davis</p>', unsafe_allow_html=True)

with col2:
    st.image("whitelogo.png", width=175)
st.markdown("___")
###################################################

col1, col2 = st.columns([3, 3])

excel_file1 = 'advanced_calculator.xlsx'
sheet_name1 = 'alladvanceddata'
sheet_name2 = 'homedefinitions'
sheet_name3 = 'speedofplay'
sheet_name4 = 'allstats'
sheet_name5 = 'wincorrelation'

df1 = pd.read_excel(excel_file1,
                   sheet_name=sheet_name2,
                   usecols='A:B',
                   header=1)
df2 = pd.read_excel(excel_file1,
                    sheet_name=sheet_name1,
                    usecols='A:T',
                    header=1)
df3 = pd.read_excel(excel_file1,
                    sheet_name=sheet_name3,
                    usecols='A:D',
                    header=2)
df4 = pd.read_excel(excel_file1,
                    sheet_name=sheet_name4,
                    usecols='A:AA',
                    header=1)
df5 = pd.read_excel(excel_file1, 
                    sheet_name=sheet_name5,
                    usecols='A:J',
                    header=1)

with col1:
    st.subheader("How to understand and use advanced stats")
    st.dataframe(df1, hide_index=True)
with col2:
    st.subheader("Pace of Play")
    st.dataframe(df3, hide_index=True, height=140)
    st.subheader("Four Factor Rating")
    st.dataframe(df5, hide_index=True)
    

st.subheader("Advanced Stats Database")
st.dataframe(df2, hide_index=True)

st.subheader("Box Score Database")
st.dataframe(df4, hide_index=True)
