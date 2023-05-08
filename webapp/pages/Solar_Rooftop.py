import pandas as pd 
import streamlit as st
import plotly.express as px

import geopandas as gpd
import plotly.graph_objects as go
import folium

from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import json

st.set_page_config(page_title='Decentralized Renewable Energy',layout='centered')
st.header('Solar Rooftop')
st.subheader('Here are some visualizations on DRE(solar rooftop)')

df= pd.read_csv(r"C:\Users\sachi\OneDrive\Desktop\webapp\data\newsolar_rooftop.csv")
df1= pd.read_csv(r"C:\Users\sachi\OneDrive\Desktop\webapp\data\solarrooftop.csv")
#gdf=gpd.read_file(r"C:\Users\sachi\OneDrive\Desktop\webapp\New_JH.geojson")
# Load GeoJSON data
with open(r"C:\Users\sachi\OneDrive\Desktop\webapp\New_JH.geojson") as f:
    geojson_data = json.load(f)

# Streamlit app
st.title('Jharkhand Districts Map')
st.subheader('Hover over the districts for more information')

# Function to customize tooltip
def style_function(feature):
    return {
        'fillColor':'green',
        'color': 'black',
        'weight': 2.5,
        'dashArray': '5, 5',
        'fillOpacity': 0.8,
    }

m = folium.Map(location=[23.6345, 85.3803], zoom_start=7, tiles='cartodbpositron')

folium.GeoJson(
    geojson_data,
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=['district','Solar_rooftop_capacity','solar_rooftop_Count'], aliases=['District:','solarrooftop capacity:','solarrooftop count:'])

).add_to(m)


folium.LayerControl().add_to(m)

st.markdown(folium_static(m))

st.write(df)
st.bar_chart(df.set_index('Dist_Name'),y='Solar_rooftop_capacity')
st.bar_chart(df.set_index('Dist_Name'),y='solar_rooftop_Count')
#st.bar_chart(df.set_index('District'),y='Financial Year')

fig3 = px.bar(df1, x='District_T', y='Financial Year ', color='Financial Year ', barmode='stack', title='Stacked Bar Chart')
fig3.update_yaxes(showticklabels=False, showgrid=False, zeroline=False)

st.plotly_chart(fig3)

fig4 = px.pie(df1, values='Capacity(In KWp)', names='District_T', color_discrete_sequence=px.colors.qualitative.Dark2,
             title='Total Capacity(kwh) in % installed on Districts of Jharkhand', hole=0.4,
             template='plotly_dark')
st.plotly_chart(fig4)

#st.write(gdf.head())
