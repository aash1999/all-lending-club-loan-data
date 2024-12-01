# Load necessary library
library(dplyr)

# Read the CSV file
input_file <- "./DataSet/cleaned_accepted_2013_to_2018Q4.csv"  # Replace with the path to your CSV file
data <- fread(input_file)

# Convert issue_d to Date format
data$issue_d <- as.Date(data$issue_d, format = "%Y-%m-%d")

# Filter data based on the conditions
filtered_data <- data %>%
  select(issue_d, loan_amnt, int_rate, grade, sub_grade, emp_length, annual_inc, 
         dti, fico_range_low, fico_range_high, last_fico_range_high, 
         last_fico_range_low, open_acc_6m, loan_status) %>%
  filter(issue_d > as.Date("2015-01-01") & loan_status == "Current")

# Save the filtered data to a new CSV file
output_file <- "predict.csv"  # Replace with your desired output file path
write.csv(filtered_data, output_file, row.names = FALSE)

cat("Filtered data saved to", output_file)
