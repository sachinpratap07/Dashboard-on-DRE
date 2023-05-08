import streamlit as st
import pandas as pd
import geopandas as gpd
import folium 
import plotly.express as px
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import json



st.set_page_config(page_title='Decentralized Renewable Energy')
st.header('MINI-GRID SOLAR STANDALONE')
st.subheader('Here are some visualizations on DRE(Mini-gridsolar standalone)')
st.warning('sorry this page is under construction')
df= pd.read_csv(r'data/Minigridsolarstandalone.csv')
#gdf=gpd.read_file(r'Jharkhand.geojson')
st.dataframe(df)

st.bar_chart(df.set_index('District'),y='Number of Household')
st.bar_chart(df.set_index('District'),y='Capacity')
#st.bar_chart(df.set_index('District'),y='Financial Year')

fig1 = px.bar(df, x='District', y='Number of Household', color='District', barmode='stack', title='Stacked Bar Chart')
fig1.update_yaxes(showticklabels=False, showgrid=False, zeroline=False)
st.plotly_chart(fig1)

fig2 = px.bar(df, x='District', y='Capacity', color='District', barmode='stack', title='Stacked Bar Chart')
fig2.update_yaxes(showticklabels=False, showgrid=False, zeroline=False)
st.plotly_chart(fig2)


fig3 = px.bar(df, x='District', y='Financial Year', color='Financial Year', barmode='stack', title='Stacked Bar Chart')
fig3.update_yaxes(showticklabels=False, showgrid=True, zeroline=True)
st.plotly_chart(fig3)


# Define the center coordinates of Jharkhand
#jharkhand_coords = [23.6102, 85.2799]


# Create a map using Folium
#m = folium.Map(location=[23.6102, 85.2799], zoom_start=8)

# Add the GeoJSON data as a layer to the map
#folium.GeoJson(gdf).add_to(m)

# Display the map in Streamlit
#st.write(m._repr_html_())


