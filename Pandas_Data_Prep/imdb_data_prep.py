import pandas as pd
import numpy as np
import re
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# ============================================================
# LOADING THE IMDB DATASET
# ============================================================
url = "https://datasets.imdbws.com/title.basics.tsv.gz"

print("Loading dataset... this may take a moment ☕")
df = pd.read_csv(
    url,
    sep='\t',
    compression='gzip',
    na_values='\\N',
    low_memory=False
)

print("Dataset loaded!")
print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())