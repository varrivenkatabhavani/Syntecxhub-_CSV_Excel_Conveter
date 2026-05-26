# csv_to_excel.py

import pandas as pd
import argparse

def convert_csv_to_excel(input_file, output_file):
    try:
        # Read CSV
        df = pd.read_csv(input_file)

        # Remove missing values
        df = df.fillna("N/A")

        # Convert column names to lowercase
        df.columns = [col.lower() for col in df.columns]

        # Save to Excel
        df.to_excel(output_file, index=False)

        print(f"Successfully converted '{input_file}' to '{output_file}'")

    except Exception as e:
        print("Error:", e)

# Command line arguments
parser = argparse.ArgumentParser(description="CSV to Excel Converter")
parser.add_argument("input", help="Input CSV file")
parser.add_argument("output", help="Output Excel file")

args = parser.parse_args()

convert_csv_to_excel(args.input, args.output)