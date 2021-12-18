import pandas as pd

ifile = "label.csv"
entities = ["obama","trump","obamacare","trumpcare","republican","democrats"]
# obama_cnt,obama_score,obama_valid

df = pd.read_csv(ifile)

for e in entities:
    count = e + "_cnt"
    score = e + "_score"
    valid = e + "_valid"
    

