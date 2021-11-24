
CREATE TABLE labels(
    index INT PRIMARY KEY,
    twitter_id INT,
    tweet_content VARCHAR(1000),
    obama_cnt INT,
    obama_score REAL,
    trump_cnt INT,
    trump_score REAL,
    obamacare_cnt INT,
    obamacare_score REAL,
    trumpcare_cnt INT,
    trumpcare_score REAL,
    republican_cnt INT,
    democrats_score REAL
);