import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Huntsville MBB Performance Analysis',
                   layout="wide", 
                   page_icon="whitelogo.png",
                   )
col1, col2 = st.columns([6, 1])
with col1:
    st.title("Multi-Stat Comparison")
    st.markdown("""
    <style>
    .big-font {font-size:15px !important;}
</style>
""", unsafe_allow_html=True)
    
    st.markdown('<p class="big-font">Compare different players by multiple stats</p>', unsafe_allow_html=True)

with col2:
    st.image("whitelogo.png", width=120)
st.markdown("___")

#################################

excel_file = 'advanced_calculator.xlsx'
sheet_name = 'alladvanceddata'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:T',
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
                    size='MP',
                    color='MP',
                    color_continuous_scale=[(0,"blue"),(0.5,"white"), (1,"red")],
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
