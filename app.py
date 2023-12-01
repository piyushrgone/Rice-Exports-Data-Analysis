import streamlit as st
import pandas as pd

df_importers = pd.read_csv('merged_data.csv')

# App layout
st.title('Rice Export Insights')
st.header('Top Importers')

# Display top importers based on Quantity of Rice Exported
st.subheader('Top Importers based on Quantity of Rice Exported')
st.table(df_importers[['IMPORTER NAME', 'QUANTITY']].head(10))