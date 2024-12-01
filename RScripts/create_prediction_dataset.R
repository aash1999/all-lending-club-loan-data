# Load necessary library
library(dplyr)

# Read the CSV file
input_file <- "./DataSet/cleaned_accepted_2013_to_2018Q4.csv"  # Replace with the path to your CSV file
df <- fread(input_file)

# Convert issue_d to Date format
df$issue_d <- as.Date(df$issue_d, format = "%Y-%m-%d")

# Filter data based on the conditions
df <- df %>%
  select(issue_d, loan_amnt, int_rate, grade, sub_grade, emp_length, annual_inc, 
         dti, fico_range_low, fico_range_high, last_fico_range_high, 
         last_fico_range_low, open_acc_6m, loan_status) %>%
  filter(issue_d > as.Date("2015-01-01") & loan_status == "Current")

df$sub_grade <- substr(df$sub_grade, 2, nchar(df$sub_grade))
df$grade <- factor(df$grade)
df$sub_grade <- factor(df$sub_grade)
df$emp_length <- factor(df$emp_length)
df$loan_status <- factor(df$loan_status)

numerical_columns <- c(
  "loan_amnt", "int_rate", "annual_inc", "dti", 
  "fico_range_low", "fico_range_high", 
  "last_fico_range_low", "last_fico_range_high", 
  "open_acc_6m"
)

# Standardize numerical columns
df[, (numerical_columns) := lapply(.SD, scale), .SDcols = numerical_columns]




# Save the filtered data to a new CSV file
output_file <- "predict.csv"  # Replace with your desired output file path
write.csv(df, output_file, row.names = FALSE)

cat("Filtered data saved to", output_file)
