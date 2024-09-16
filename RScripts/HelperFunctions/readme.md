# Helper Functions

This folder contains a collection of useful helper functions that you may use in your projects. Each function is stored in a separate `.R` file, and you can import any function into your R scripts or R Markdown files as needed.

## How to Use

To use any function from this collection, you can import the corresponding `.R` file using the `source()` function in R. Below is a table that lists each function, the parameters it accepts, the return type, and a brief description.

### Usage Example
```r
# Importing a function from the helper function folder
source('path_to_helper_function_folder/your_function.R')

# Example: calling the function
result <- your_function(arg1, arg2)
print(result)
```

### Function Table

| Function Name | How to Import                          | Parameters                     | Return Type |        Description                               |
|---------------|----------------------------------------|---------------------------------|-------------|-------------------------------------------|
| `fetch_subset` | `source("./HelperFunctions/fetchSubset.R")` | `df_location`: char (required) <br>`col_names`: vector (required) <br> `nrows` : vector (default c(1,-1))    | `data.table()`     | Fetches the subset from large CSV files          |
