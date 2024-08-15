import pandas as pd
from datetime import datetime
import os

# Load the Excel file
file_path = r'C:\Users\oossa\Desktop\Financial Reports\Ages Of Supplier Debts\Ages of supplier debts.xlsx'
excel_data = pd.read_excel(file_path)

# Convert the 'Date' column to datetime format if necessary
excel_data['last payment'] = pd.to_datetime(excel_data['Date'], errors='coerce')

# Function to create separate Excel files based on year and month
def separate_excel_by_year_month(data):
    # Ensure the output directory exists
    output_dir = 'output_files'  # Replace with your desired directory path
    os.makedirs(output_dir, exist_ok=True)

    # Group data by year and month
    data['Year'] = data['Date'].dt.year
    data['Month'] = data['Date'].dt.month
    grouped = data.groupby(['Year', 'Month'])

    for (year, month), group in grouped:
        if pd.notna(year) and pd.notna(month):
            output_file = os.path.join(output_dir, f'data_{year}_{month:02}.xlsx')
            try:
                # Write data to the output file
                group.to_excel(output_file, index=False, sheet_name=f'{year}_{month:02}')
                print(f'File {output_file} written successfully')
            except Exception as e:
                print(f'Error writing to {output_file}: {e}')

# Call the function to separate the data
separate_excel_by_year_month(excel_data)
