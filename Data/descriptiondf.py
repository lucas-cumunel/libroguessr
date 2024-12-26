import pandas as pd

books = r"Data\base_csv_final.csv"
df = pd.read_csv(books)
print(df.shape)