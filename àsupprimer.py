import pandas as pd
base = r'Data\base_csv_final.csv'
df = pd.read_csv(base)

print(df.iloc[45])
