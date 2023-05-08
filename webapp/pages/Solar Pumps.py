import pandas as pd 
import streamlit as st
import plotly.express as px
from PIL import Image
import geopandas as gpd
 
st.set_page_config(page_title='Decentralized Renewable Energy')
st.header('SOLAR PUMPS')
st.subheader('Here are some visualizations on DRE(Solar Pumps)')

df= pd.read_csv(r'C:\Users\sachi\OneDrive\Desktop\webapp\data\solarpump.csv')
gdf=gpd.read_file(r'Jharkhand.geojson')
st.write(df)
st.bar_chart(df.set_index('District'), y='Districtwise_Solar_pumps_Installed_(Till now)')
#st.bar_chart(df.set_index('District'),y='Capacity')
#st.bar_chart(df.set_index('District'),y='Financial Year')


fig1 = px.bar(df, x='District', y='Districtwise_Solar_pumps_Installed_(Till now)', color='District', barmode='stack', title='Stacked Bar Chart')
fig1.update_yaxes(showticklabels=False, showgrid=False, zeroline=False)
st.plotly_chart(fig1)

fig4 = px.pie(df, values='Districtwise_Solar_pumps_Installed_(Till now)', names='District', color_discrete_sequence=px.colors.qualitative.Dark2,
             title='Total solar pumps installed till now on Districts of Jharkhand', hole=0.4,
             template='plotly_dark')
st.plotly_chart(fig4)

