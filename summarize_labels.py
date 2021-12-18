import pandas as pd

ifile = "label.csv"
ofile = "positive_negative_data.csv"
entities = ["obama","trump","obamacare","trumpcare","republican","democrats"]
tweet_field = "tweet_content"
# obama_cnt,obama_score,obama_valid

df = pd.read_csv(ifile)

s_list = list()
e_list = list()
pos_neg = list()

tweets = list(df[tweet_field].values)

for e in entities:
    count_field = e + "_cnt"
    score_field = e + "_score"
    valid_field = e + "_valid"

    count = list(df[count_field].values)
    score = list(df[score_field].values)
    valid = list(df[valid_field].values)

    for c,s,v,t in zip(count, score, valid,tweets):
        if v == 0: continue # not valid
        if c == 0: continue # not assigned
        pns = -1 if s < 0 else 1
        s_list.append(t)
        e_list.append(e)
        pos_neg.append(pns)

data = {"sentence": s_list, "entities": e_list, "positive_negative": pos_neg}
df = pd.DataFrame(data=data)
df.to_csv(ofile, index=None)



