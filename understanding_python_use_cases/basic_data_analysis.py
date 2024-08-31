
# Use Pandas to read a CSV file and print the first five rows.

import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())