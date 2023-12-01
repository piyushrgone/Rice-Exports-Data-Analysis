import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('merged_data.csv')

# App layout
st.set_page_config(layout="wide") 
st.title('Rice Export Insights')
st.header('Top Importers')

# Sidebar with different sections
selected_section = st.sidebar.radio('Select Section', ['Import/Export Analysis', 'Geographical Analysis', 'Product Analysis', 'Financial', 'Time Series', 'Key Insights'])

# Section: Import/Export Analysis
if selected_section == 'Import/Export Analysis':
    col1, col2 = st.columns(2)
    
    col1.header('Import/Export Analysis Section')
    # Section: Top Importers based on Import Value (CIF)
    col1.header('Top Importers based on Import Value (CIF)')
    top_importers_value = df.groupby('IMPORTER NAME')['IMPORT VALUE CIF'].sum().sort_values(ascending=False).head(10)
    col1.table(top_importers_value)

    # Section: Top Importers based on Quantity of Rice Exported
    col1.header('Top Importers based on Quantity of Rice Exported')
    top_importers_quantity = df.groupby('IMPORTER NAME')['QUANTITY'].sum().sort_values(ascending=False).head(10)
    col1.table(top_importers_quantity)

    # Section: Top Exporters based on Import Value (CIF)
    col1.header('Top Exporters based on Import Value (CIF)')
    top_exporters_value = df.groupby('EXPORTER NAME')['IMPORT VALUE CIF'].sum().sort_values(ascending=False).head(10)
    col1.table(top_exporters_value)

    # Section: Top Exporters based on Quantity of Rice Exported
    col1.header('Top Exporters based on Quantity of Rice Exported')
    top_exporters_quantity = df.groupby('EXPORTER NAME')['QUANTITY'].sum().sort_values(ascending=False).head(10)
    col1.table(top_exporters_quantity)

    col2.header('Top Importers by Import Value')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='IMPORT VALUE CIF', y='IMPORTER NAME', data=df.sort_values('IMPORT VALUE CIF', ascending=False).head(10), ax=ax)
    col2.pyplot(fig)

    col2.header('Top Importers by Quantity')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='QUANTITY', y='IMPORTER NAME', data=df.sort_values('QUANTITY', ascending=False).head(20), ax=ax)
    col2.pyplot(fig)
    
    col2.header('Top Exporters by Import Value')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='IMPORT VALUE CIF', y='EXPORTER NAME', data=df.sort_values('IMPORT VALUE CIF', ascending=False).head(10), ax=ax)
    col2.pyplot(fig)
        
    col2.header('Top Exporters by Quantity')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='QUANTITY', y='EXPORTER NAME', data=df.sort_values('QUANTITY', ascending=False).head(20), ax=ax)
    col2.pyplot(fig)
    
# Section: Geographical Analysis
elif selected_section == 'Geographical Analysis':
    st.header('Geographical Analysis Section')
    # Add your analysis and visualizations here

# Section: Product Analysis
elif selected_section == 'Product Analysis':
    st.header('Product Analysis Section')
    # Add your analysis and visualizations here

# Section: Financial
elif selected_section == 'Financial':
    st.header('Financial Section')
    # Add your analysis and visualizations here

# Section: Time Series
elif selected_section == 'Time Series':
    st.header('Time Series Section')
    # Add your analysis and visualizations here

# Section: Key Insights
elif selected_section == 'Key Insights':
    st.header('Key Insights Section')
    # Add your analysis and visualizations here
    st.write("This is where you can highlight key insights.")