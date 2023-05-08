import pandas as pd 
import streamlit as st
import plotly.express as px
from PIL import Image
import geopandas as gpd
 
st.set_page_config(page_title='Decentralized Renewable Energy')
st.header('SOLAR GROUND MOUNTED PLANTS')
st.subheader('Here are some visualizations on(Solar Ground Mounted Plants)')

df= pd.read_csv(r'C:\Users\sachi\OneDrive\Desktop\webapp\data\solargroundmounted.csv')
gdf=gpd.read_file(r'Jharkhand.geojson')

st.dataframe(df)
st.bar_chart(df.set_index('District'),y='Capacity (kWp)')
#st.bar_chart(df.set_index('District'),y='Capacity')
#st.bar_chart(df.set_index('District'),y='Financial Year')

