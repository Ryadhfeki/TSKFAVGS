
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# Streamlit app converted from Colab notebook

# Display Title and Descriptions
st.title("Purchasing Data 2024 - Commande BO")
st.markdown("**PDATA Orders Analysis**")
st.markdown("---")
st.write("This application converts Order data to include categories purchased in each Order.")

# Placeholder for file upload
uploaded_file = st.file_uploader("Upload the 2024 Purchasing Data Excel file", type=["xlsx"])

# Function to process the uploaded file
def process_data(file):
    # Assuming data sheet or necessary sheet will be read from this uploaded file
    data = pd.read_excel(file, sheet_name=0)  # Adjust the sheet name or index as needed
    # Process the data (example operation)
    data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')  # Example column
    data['Order Month'] = data['Order Date'].dt.to_period("M")
    
    # Sample plot
    fig = px.histogram(data, x='Order Month', title='Orders by Month')
    st.plotly_chart(fig)
    return data

# Process and display if file is uploaded
if uploaded_file:
    data = process_data(uploaded_file)
    st.write("Preview of processed data:")
    st.write(data.head())

# Additional analysis or visualization
# Example - Orders by Category Plot
if uploaded_file:
    st.subheader("Order Category Analysis")
    fig = px.bar(data, x='Category', y='Order Value', title="Order Value by Category")
    st.plotly_chart(fig)

st.markdown("---")
st.write("End of Analysis")
