import streamlit as st
import pandas as pd
import numpy as np
import os

from urllib.request import urlopen
import json
from PIL import Image

import plotly.express as px

# Load counties geojson data
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# Set page configuration
st.set_page_config(
    page_title="AQUA NET",
    page_icon="👋",
)

# Title and logo
col1, col2 = st.columns([2, 8])
with col1:
    # Load logo image
    image = Image.open(f'{os.getcwd()}/Aqua.jpg')
    st.image(image, caption='', width=100)
with col2:
    st.title("AQUA NET")
    st.sidebar.success("Select a page above.")

# File uploader for data
st.subheader('Please upload Data file for a particular region')
st.markdown("---")
data_file = st.file_uploader("Select file", type=["csv"])

# Read data if file uploaded
if data_file is not None:
    df = pd.read_csv(data_file)
    st.dataframe(df)

    # Update code column to have leading zero
    df['CODE'] = df["CODE"].apply(lambda x: '0' + str(x))

    # Create choropleth map
    fig = px.choropleth_mapbox(df, geojson=counties, locations='CODE', color='SANITATION TECH.',
                                mapbox_style="carto-positron",
                                zoom=3, center={"lat": 37.0902, "lon": -95.7129},
                                opacity=0.5,
                                labels={'unemp': 'unemployment rate'}
                                )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    # Display map in expander
    with st.expander("Result on Map", expanded=False):
        st.plotly_chart(fig)

    
