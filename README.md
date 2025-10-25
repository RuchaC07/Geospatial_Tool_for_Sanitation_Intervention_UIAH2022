# Geospatial Tool for Sanitation Intervention UIAH2022

## Overview
An predictive decision support tool that leverages **geospatial data** to recommend optimal **sanitation techniques** across diverse terrains. It integrates **regional environmental and demographic datasets** to deliver data-driven, location-specific, and sustainable sanitation insights. This is a crucial problem statement for both the countries, India and Africa.

## Key Features
- Predictive model for sanitation recommendation  
- Integration of regional and geospatial datasets  
- Interactive visualization using Streamlit and Plotly  
- Google Sheets connectivity for live data retrieval  

## Tech Stack
**Python | Streamlit | Altair | Plotly | OpenPyXL | GSheetsDB**

## Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/<your-username>/sanitation-decision-tool.git
   cd sanitation-decision-tool
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

   **requirements.txt**
   ```
   streamlit==1.11.0
   altair<5
   plotly
   gsheetsdb
   openpyxl
   ```

3. Run the Streamlit app:  
   ```bash
   streamlit run app.py
   ```

## Usage
Upload your regional dataset or connect via Google Sheets to generate AI-driven sanitation recommendations and visualize suitability maps interactively, here the dataset is used from kaggle and information is taken form ArcGIS.

## Author
**Rucha Rangnath Choudhari**  
