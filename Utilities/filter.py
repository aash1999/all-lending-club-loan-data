import pandas as pd

def filter_large_csv(file_path, date_col, date_threshold, chunk_size=1e6, output_path=None):
    """
    Reads a large CSV file in chunks, filters rows based on the date column,
    and returns a DataFrame with rows where the date is greater than the threshold.
    
    Parameters:
    - file_path (str): Path to the CSV file.
    - date_col (str): Name of the date column.
    - date_threshold (str): Date threshold in 'YYYY-MM-DD' format.
    - chunk_size (float): Number of rows per chunk. Default is 1e6 (1 million).
    - output_path (str or None): If provided, saves the filtered DataFrame to a CSV file.
    
    Returns:
    - pd.DataFrame: Filtered DataFrame with rows where the date is greater than the threshold.
    """
    # Initialize an empty list to hold the filtered chunks
    filtered_chunks = []

    # Define the date threshold
    date_threshold = pd.to_datetime(date_threshold)

    # Read the CSV file in chunks
    for chunk in pd.read_csv(file_path, chunksize=chunk_size, parse_dates=[date_col], infer_datetime_format=True):
        # Filter rows based on the date threshold
        filtered_chunk = chunk[chunk[date_col] > date_threshold]
        filtered_chunks.append(filtered_chunk)
    
    # Concatenate all filtered chunks into a single DataFrame
    filtered_df = pd.concat(filtered_chunks, ignore_index=True)
    
    # Optionally save the filtered DataFrame to a new CSV file
    if output_path:
        filtered_df.to_csv(output_path, index=False)
    
    return filtered_df

# Define parameters
file_path = './DataSet/rejected_2007_to_2018Q4.csv'
date_col = 'Application Date'  # Column name
date_threshold = '2013-01-01'  # Date threshold
output_path = './DataSet/filtered_rejected_2013_to_2018Q.csv'  # Path to save the filtered data

# Apply the function
filtered_df = filter_large_csv(file_path, date_col, date_threshold, output_path=output_path)

# Print the number of rows after filtering
print(f"Number of rows after filtering: {len(filtered_df)}")

import pandas as pd

def filter_large_csv(file_path, date_col, date_format, date_threshold, chunk_size=1e6, output_path=None):
    """
    Reads a large CSV file in chunks, filters rows based on the date column,
    and returns a DataFrame with rows where the date is greater than the threshold.
    
    Parameters:
    - file_path (str): Path to the CSV file.
    - date_col (str): Name of the date column.
    - date_format (str): Format of the dates in the column.
    - date_threshold (str): Date threshold in 'YYYY-MM-DD' format.
    - chunk_size (float): Number of rows per chunk. Default is 1e6 (1 million).
    - output_path (str or None): If provided, saves the filtered DataFrame to a CSV file.
    
    Returns:
    - pd.DataFrame: Filtered DataFrame with rows where the date is greater than the threshold.
    """
    # Initialize an empty list to hold the filtered chunks
    filtered_chunks = []

    # Define the date threshold
    date_threshold = pd.to_datetime(date_threshold)

    # Read the CSV file in chunks
    for chunk in pd.read_csv(file_path, chunksize=chunk_size, parse_dates=[date_col], date_parser=lambda x: pd.to_datetime(x, format=date_format)):
        # Filter rows based on the date threshold
        filtered_chunk = chunk[chunk[date_col] > date_threshold]
        filtered_chunks.append(filtered_chunk)
    
    # Concatenate all filtered chunks into a single DataFrame
    filtered_df = pd.concat(filtered_chunks, ignore_index=True)
    
    # Optionally save the filtered DataFrame to a new CSV file
    if output_path:
        filtered_df.to_csv(output_path, index=False)
    
    return filtered_df

# Define parameters
file_path = './DataSet/accepted_2007_to_2018Q4.csv'
date_col = 'issue_d'  # Column name
date_format = '%b-%Y'  # Date format in the dataset (e.g., Aug-2003)
date_threshold = '2013-01-01'  # Date threshold
output_path = './DataSet/filtered_accepted_2013_to_2018Q4.csv'  # Path to save the filtered data

# Apply the function
filtered_df = filter_large_csv(file_path, date_col, date_format, date_threshold, output_path=output_path)

# Print the number of rows after filtering
print(f"Number of rows after filtering: {len(filtered_df)}")

