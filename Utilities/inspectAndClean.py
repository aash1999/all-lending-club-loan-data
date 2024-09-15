import pandas as pd

def analyze_and_clean_dataset(file_path, output_txt, output_csv, null_threshold=0.7):
    """
    Reads a CSV file, saves column data types and null counts to a .txt file, 
    removes columns with more than the specified threshold of null values, 
    removes rows with all null values or with fewer than 4 non-null values, and saves the cleaned DataFrame to a new CSV.

    Parameters:
    - file_path (str): Path to the input CSV file.
    - output_txt (str): Path to the output .txt file to save column details and information about dropped rows/columns.
    - output_csv (str): Path to save the cleaned DataFrame as a new CSV file.
    - null_threshold (float): Threshold to drop columns with more than the specified percentage of null values.
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Get data types of each column
    dtypes = df.dtypes
    
    # Get the number of null values in each column
    null_values = df.isnull().sum()
    
    # Calculate the percentage of null values for each column
    null_percent = (null_values / len(df)) * 100
    
    # Save data types and null values information to a .txt file
    with open(output_txt, 'w') as f:
        f.write(f"Data types for {file_path}:\n")
        f.write(dtypes.to_string())
        f.write("\n\n")
        f.write(f"Number of null values in {file_path}:\n")
        f.write(null_values.to_string())
        f.write("\n\n")
        f.write(f"Percentage of null values in {file_path}:\n")
        f.write(null_percent.to_string())
    
    # Drop columns with more than 80% null values
    columns_to_drop = null_percent[null_percent > (null_threshold * 100)].index
    df_cleaned = df.drop(columns=columns_to_drop)
    
    # Save information about dropped columns
    with open(output_txt, 'a') as f:
        f.write(f"\nDropped columns ({len(columns_to_drop)}):\n")
        f.write(", ".join(columns_to_drop))
        f.write("\n\n")
    
    # Filter out rows with all null values
    rows_all_null = df_cleaned[df_cleaned.isnull().all(axis=1)]
    df_cleaned = df_cleaned.dropna(how='all')
    
    # Filter out rows with fewer than 4 non-null values
    rows_few_values = df_cleaned[df_cleaned.notnull().sum(axis=1) < 4]
    df_cleaned = df_cleaned[df_cleaned.notnull().sum(axis=1) >= 4]
    
    # Save dropped rows information to the .txt file
    with open(output_txt, 'a') as f:
        f.write(f"\nDropped rows with all null values: {len(rows_all_null)}\n")
        f.write(f"Dropped rows with fewer than 4 non-null values: {len(rows_few_values)}\n")
        f.write("\nSample of dropped rows:\n")
        f.write(rows_few_values.head().to_string())  # Save sample rows to the file
    
    # Save the cleaned DataFrame to a new CSV file
    df_cleaned.to_csv(output_csv, index=False)
    
    print(f"Cleaned dataset saved to {output_csv}")

# Define file paths
file_accepted = './DataSet/filtered_accepted_2013_to_2018Q4.csv'
file_rejected = './DataSet/filtered_rejected_2013_to_2018Q.csv'

# Define output paths for analysis
output_txt_accepted = './DataSet/accepted_analysis.txt'
output_csv_accepted = './DataSet/cleaned_accepted_2013_to_2018Q4.csv'

output_txt_rejected = './DataSet/rejected_analysis.txt'
output_csv_rejected = './DataSet/cleaned_rejected_2013_to_2018Q4.csv'

# Analyze and clean the accepted dataset
print("=== Accepted Dataset ===")
analyze_and_clean_dataset(file_accepted, output_txt_accepted, output_csv_accepted)

# Analyze and clean the rejected dataset
print("=== Rejected Dataset ===")
analyze_and_clean_dataset(file_rejected, output_txt_rejected, output_csv_rejected)
