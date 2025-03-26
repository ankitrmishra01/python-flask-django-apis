import csv

def calculate_average(csv_file, column_name):
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print("Available columns:", reader.fieldnames)  # Debugging
            
            values = []
            for row in reader:
                if column_name in row:
                    try:
                        value = float(row[column_name].strip())  # Remove spaces & convert
                        values.append(value)
                    except ValueError:
                        print(f"Skipping non-numeric value: {repr(row[column_name])}")
            
            if values:
                return f"Average of column '{column_name}': {sum(values) / len(values):.2f}"
            else:
                return "No numeric values found in the specified column."
    
    except FileNotFoundError:
        return "Error: File not found!"
    except KeyError:
        return "Error: Column name not found in the file!"

# Example usage
csv_file = "data.csv"
column_name = "Price"  # Replace with the exact column name

print(calculate_average(csv_file, column_name))

