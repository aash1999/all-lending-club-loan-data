library(data.table)

# Function to load specific rows and columns efficiently
  # Function to load specific rows and columns efficiently
  # 
  # This function reads specific rows and columns from a large CSV file using 
  # chunk-based reading to handle large datasets without consuming excessive memory.
  # It supports fetching the first N rows, the last N rows, a range of rows, or all rows.
  #
  # Arguments:
  #   df_location: The file path to the CSV file that contains the data. (character)
  #   col_names: A vector of column names to be selected from the dataset. (character)
  #   nrows: A vector specifying which rows to fetch. (numeric or integer)
  #          - c(1, n): Fetch the first `n` rows.
  #          - c(n, -1): Fetch the last `n` rows.
  #          - c(m, n): Fetch rows from `m` to `n` (both inclusive). DEFAULT
  #          - c(1, -1): Fetch all rows from the first to the last.
  #          Default is `c(1, -1)` to fetch all rows.
  #   chunk_size: Here's the revised version: The size of a single chunk. If the chunk size is too large, you might encounter a memory error. The default is 1e5.
  #
  # Returns:
  #   A `data.table` containing the subset of rows and columns from the CSV file.
  #
  # Example usage:
  #   source("./HelperFunctions/fetchSubset.R")
  #   df_location = "../DataSet/xxx.csv"
  #   col_names = c("loan_status", "gpa")
  #   nrows = c(1, 100)  # Fetch rows 1 to 100
  #   result_df = fetch_subset(df_location, col_names, nrows)

fetch_subset <- function(df_location, col_names, nrows = c(1, -1), chunk_size = 1e5) {
    
  # Step 1: Read the first chunk to determine column indices and header information
  first_chunk <- fread(df_location, nrows = chunk_size, header = TRUE)
  all_col_names <- names(first_chunk)  # Extract all column names
  
  
  # Error handling if some column names are not

  # Chunk size set to 1e5 for large datasets
  chunk_size <- 1e5
  
  # Read the first chunk to determine column indices
  first_chunk <- fread(df_location, nrows = chunk_size, header = TRUE)
  all_col_names <- names(first_chunk)
  # Convert column names to column indices
  if (length(col_names) == 1 & col_names[1] == -1){
    col_indices <- which(all_col_names %in% all_col_names)
  }else{
    col_indices <- which(all_col_names %in% col_names) 
  }
  
  
  # Determine the range of rows to fetch
  if (length(nrows) == 2) {
    if (nrows[2] == -1) {
      # Fetch the last n rows
      total_rows <- nrow(fread(df_location, select = 1, header = TRUE))  # Count total rows
      row_start <- nrows[1]
      row_end <- total_rows
    } else {
      # Fetch rows from m to n
      row_start <- nrows[1]
      row_end <- nrows[2]
    }
  } else if (length(nrows) == 1 && nrows[1] == -1) {
    # Fetch all rows
    row_start <- 1
    row_end <- -1
  } else {
    stop("Invalid nrows format. Please use c(m, n), c(1, -1) for all rows.")
  }
  
  # Total number of rows (if not fetching all rows)
  total_rows <- if (row_end != -1) nrow(fread(df_location, select = 1, header = TRUE)) else -1
  
  # Initialize result data table
  result <- data.table()
  
  # Reading data in chunks
  current_row <- 1
  while (TRUE) {
    # Check if the skip parameter exceeds the number of rows
    if (total_rows != -1 && current_row > total_rows) break
    
    # Read a chunk with specified columns
    chunk <- fread(df_location, select = col_indices, skip = max(0, current_row - 1), nrows = chunk_size, header = FALSE)
    
    if (nrow(chunk) == 0) break  # Stop if no more data to read
    
    # Check if the chunk contains rows within the required range
    if (row_end == -1 || (row_start <= current_row + nrow(chunk) - 1 && current_row <= row_end)) {
      # Determine the subset of rows in the chunk
      row_subset_start <- max(1, row_start - current_row + 1)
      row_subset_end <- min(nrow(chunk), row_end - current_row + 1)
      
      # Append the required rows to the result
      result <- rbind(result, chunk[row_subset_start:row_subset_end, ])
      
      # Stop if the required number of rows is fetched
      if (row_end != -1 && current_row + nrow(chunk) - 1 >= row_end) break
    }
    
    current_row <- current_row + chunk_size  # Move to the next chunk
  }
  
  # Set column names to result based on first chunk
  setnames(result, all_col_names[col_indices])
  
  return(result)
}

# Usage example:
# df_location = "path_to_file.csv"
# col_names = c("loan_status")  # Replace with actual column names you want
# nrows = c(1, -1)  # Fetch all rows from the first to the last
# result_df = fetch_subset(df_location, col_names, nrows)
