import pandas as pd

df = pd.read_csv("selected_subset.csv")
df = df.drop("idx",1)

df.to_csv("selected_subset.csv", index=None)