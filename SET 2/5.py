import pandas as pd
from tabulate import tabulate

def read_excel(file_path, sheet_name=0):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        # Print the data in a tabular format
        print(tabulate(df, headers='keys', tablefmt='grid'))
    except Exception as e:
        print(f"Error: {e}")

# Example usage
file_path = "example1.xls"  # Replace with your file path
read_excel(file_path)
