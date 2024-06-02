import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Huntsville MBB Performance Analysis',
                   layout="wide", 
                   page_icon="whitelogo.png",
)
st.header('Multi-Stat Comparsion Plot')

excel_file = 'analytics_database.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:R',
                   header=1)

col1, col2 = st.columns([3, 2])

with col2:
    x_column = st.selectbox("Select X Axis", df.columns.tolist(), placeholder="Select Statistic")
    y_column = st.selectbox("Select Y Axis", df.columns.tolist(), placeholder="Select Statistic")
    player_filter = st.multiselect('Select Player', options=list(df['Player'].unique()),)
    opponent_filter = st.multiselect('Select Opponent', options=list(df['Opponent'].unique()),)

filtered_data = df[df['Player'].isin(player_filter) & df['Opponent'].isin(opponent_filter)]
with col1:
    st.subheader("Player Comparison Scatter Plot:")
    fig = px.scatter(filtered_data, 
                    x=x_column, 
                    y=y_column,
                    hover_data={'Player': True},
                    template='plotly',
                    )   

    fig.update_traces(mode="markers") 
    fig.update_layout(
        hoverlabel=dict(
         bgcolor="Navy", 
         font_size=16,
         font_color="White",
     )
    )  

    st.plotly_chart(fig, use_container_width=True)
