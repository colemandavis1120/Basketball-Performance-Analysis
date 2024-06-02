import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Huntsville MBB Performance Analysis',
                   layout="wide", 
                   page_icon="whitelogo.png",
                   )
col1, col2 = st.columns([6, 1])
with col1:
    st.title("Player Impact Comparison")
    st.markdown("""
    <style>
    .big-font {font-size:13px !important;}
</style>
""", unsafe_allow_html=True)
    
    st.markdown('<p class="big-font">Compare the impact and usage of different players</p>', unsafe_allow_html=True)

with col2:
    st.image("whitelogo.png", width=120)
st.markdown("___")

#################################

excel_file = 'analytics_database.xlsx'
sheet_name = 'piedata'

df1 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:C',
                   header=1)
df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='E:G',
                   header=1)

player_filter = st.multiselect('Select Player', options=list(df1['Player'].unique()),)
opponent_filter = st.multiselect('Select Opponent', options=list(df1['Opponent'].unique()),)
filtered_data = df1[df1['Player'].isin(player_filter) & df1['Opponent'].isin(opponent_filter)]

st.subheader("Player Impact Estimate (PIE)")
fig = px.pie(filtered_data, values='PIE', names='Player')
st.plotly_chart(fig, use_container_width=True)


#player_filter2 = st.multiselect('Select Player', options=list(df2['Player'].unique()),)
#opponent_filter2 = st.multiselect('Select Opponent', options=list(df2['Opponent'].unique()),)
#filtered_data2 = df2[df2['Player'].isin(player_filter2) & df2['Opponent'].isin(opponent_filter2)]

#st.subheader("Player Usage %")
#fig = px.pie(filtered_data2, values='PIE', names='Player')
#st.plotly_chart(fig, use_container_width=True)
