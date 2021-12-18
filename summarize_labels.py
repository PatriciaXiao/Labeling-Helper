import pandas as pd

ifile = "label.csv"
entities = ["obama","trump","obamacare","trumpcare","republican","democrats"]
# obama_cnt,obama_score,obama_valid

df = pd.read_csv(ifile)

print(df)

