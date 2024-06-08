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
    st.title("Performance vs Minutes Played")
    st.header('2024-2025')
    st.markdown("""
    <style>
    .big-font {font-size:15px !important;}
</style>
""", unsafe_allow_html=True)
    
st.markdown('<p class="big-font">Analyze player performance compared to their playing time</p>', unsafe_allow_html=True)

with col2:
    st.image("whitelogo.png", width=175)
st.markdown("___")
###################################################

col1, col2 = st.columns([3, 1])

excel_file1 = 'advanced_calculator.xlsx'
sheet_name1 = 'alladvanceddata'

df = pd.read_excel(excel_file1,
                    sheet_name=sheet_name1,
                    usecols='B:S',
                    header=1)

with col2: 
    x_column = st.selectbox("Select Statistic", df.columns.tolist(), placeholder="Select Statistic")
    opponent_filter = st.multiselect('Select Opponent', options=list(df['Opponent'].unique()),)
    player_filter = st.multiselect('Select Player', options=list(df['Player'].unique()),)

filtered_data = df[df['Player'].isin(player_filter) & df['Opponent'].isin(opponent_filter)]
with col1:
    st.subheader('Performance vs Minutes Played')
    fig = px.bar(filtered_data, x='Player', y=x_column,
                 hover_data=['MP'], color='MP',
                 color_continuous_scale=[(0,"blue"),(0.5,"white"), (1,"red")],
                 height=400)
    st.plotly_chart(fig, use_container_width=True)
