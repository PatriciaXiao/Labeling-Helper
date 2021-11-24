CREATE SCHEMA debug;

CREATE TABLE debug.table1(
    val1 INT PRIMARY KEY,
    val2 INT NOT NULL,
    val3 VARCHAR(1000)
);

INSERT INTO debug.table1 (val1, val2, val3)
VALUES (1, 2, "hello world");

INSERT INTO debug.table1 (val2, val3)
VALUES (10, "hello world 10");