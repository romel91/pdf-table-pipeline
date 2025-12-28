import tabula
import camelot
import pandas as pd

# Step 1: Read all tables
tables = tabula.read_pdf('BBSData.pdf', stream =True, pages='all')

# Step 2: Filter tables containing "Table 3.8.1" in the first few rows
tables_filtered = []
for table in tables:
    df = table.df  # the DataFrame
    if df.astype(str).apply(lambda x: x.str.contains("Table 3.8.1")).any().any():
        tables_filtered.append(table)

# Step 3: Export filtered tables to CSV
for i, table in enumerate(tables_filtered):
    table.to_csv(f'bbs_table_3_8_1_{i}.csv')