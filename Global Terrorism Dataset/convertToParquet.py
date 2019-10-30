import pandas as pd
df = pd.read_csv('globalterrorismdb_0718dist.csv', encoding='ISO-8859-1')
df.to_parquet('globalterrorismdb')
print(df.shape)