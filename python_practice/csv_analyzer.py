import pandas as pd

file_name = input("Enter the CSV file name:")

df = pd.read_csv(file_name)

print("\nCSV Loaded Successfully!")

print("\nTotal Rows and Columns:")

