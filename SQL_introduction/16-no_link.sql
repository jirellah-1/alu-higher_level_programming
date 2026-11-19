-- Lists the score and the name of all records of second_table that have a name, best first.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
