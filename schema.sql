CREATE TABLE labels(
    index INT PRIMARY KEY,
    twitter_id TEXT,
    tweet_content TEXT,
    obama_cnt INT,
    obama_score REAL,
    trump_cnt TEXT,
    trump_score REAL,
    obamacare_cnt TEXT,
    obamacare_score REAL,
    trumpcare_cnt TEXT,
    trumpcare_score REAL,
    republican_cnt TEXT,
    democrats_score REAL
);