import pandas as pd
import os

def create_dataframe(file_path):
    file_path = file_path.strip('"').strip("'")
    
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".csv":
        return pd.read_csv(file_path)
    elif ext in [".xls", ".xlsx"]:
        return pd.read_excel(file_path)
    elif ext == ".json":
        return pd.read_json(file_path)
    elif ext == ".parquet":
        return pd.read_parquet(file_path)
    elif ext == ".html":
        return pd.read_html(file_path)[0]
    elif ext == ".xml":
        return pd.read_xml(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")