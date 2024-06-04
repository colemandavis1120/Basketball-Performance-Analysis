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

excel_file = 'analytics_database.xlsx'
sheet_name = 'trenddata'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:S',
                   header=1)

col1, col2 = st.columns([4, 1])

with col2:
    y_column = st.selectbox("Select Y Axis", df.columns.tolist(), placeholder="Select Statistic")
    player_filter = st.multiselect('Select Player', options=list(df['Player'].unique()),)

filtered_data = df[df['Player'].isin(player_filter)]

#fig = px.line(filtered_data, x="Opponent", y=y_column)

with col1: 
    fig = px.line(filtered_data, x="Opponent", y=y_column, color='Player')
    st.plotly_chart(fig, use_container_width=True)
