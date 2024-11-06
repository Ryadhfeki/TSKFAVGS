import pandas as pd

def handle_file_upload(uploaded_file):
    """Handles file uploads and returns a DataFrame."""
    try:
        return pd.read_excel(uploaded_file)
    except Exception as e:
        raise ValueError(f"Error loading file: {e}")
