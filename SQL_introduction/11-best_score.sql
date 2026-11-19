-- Lists the score and the name of all records of second_table with a score >= 10, best first.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
