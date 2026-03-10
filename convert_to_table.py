import pandas as pd

# Read the CSV file
df = pd.read_csv('dataset/hr_attrition_cleaned_data.csv')

# Display as markdown table
print(df.head(20).to_markdown(index=False))

