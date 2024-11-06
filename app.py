import streamlit as st
import pandas as pd
from utils.data_processing import process_monthly_data, generate_client_purchases_summary
from utils.file_helpers import handle_file_upload

st.title("Average Spend Task Force App")

# Upload files
st.sidebar.header("Upload Data Files")
orders_file = st.sidebar.file_uploader("Upload Orders File (e.g., orders.xlsx)", type="xlsx")
pdata_file = st.sidebar.file_uploader("Upload PDATA File (e.g., pdata.xlsx)", type="xlsx")
segmentation_file = st.sidebar.file_uploader("Upload Segmentation File (e.g., segmentation.xlsx)", type="xlsx")

if orders_file and pdata_file and segmentation_file:
    # Load the data files
    orders_df = handle_file_upload(orders_file)
    pdata_df = handle_file_upload(pdata_file)
    segmentation_df = handle_file_upload(segmentation_file)
    
    # Run the processing functions
    st.write("Processing data for last three months...")
    try:
        monthly_results = process_monthly_data(orders_df, pdata_df, segmentation_df)
        
        # Display each monthly result and provide download link
        for month, result in monthly_results.items():
            st.subheader(f"Processed Data for {month}")
            st.dataframe(result)
            csv = result.to_csv(index=False)
            st.download_button(
                label=f"Download Processed Data for {month}",
                data=csv,
                file_name=f"processed_data_{month}.csv",
                mime="text/csv"
            )
        
        # Generate and display client purchases summary
        client_summary = generate_client_purchases_summary(monthly_results)
        st.subheader("Client Purchases Summary")
        st.dataframe(client_summary)
        csv_summary = client_summary.to_csv(index=False)
        st.download_button(
            label="Download Client Purchases Summary",
            data=csv_summary,
            file_name="client_purchases_summary.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"Error processing files: {e}")
else:
    st.warning("Please upload all required files to proceed.")
