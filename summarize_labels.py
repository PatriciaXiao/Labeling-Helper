import pandas as pd

ifile = "label.csv"

entities = ["obama","trump","obamacare","trumpcare","republican","democrats"]

df = pd.read_csv(ifile)

print(df)

