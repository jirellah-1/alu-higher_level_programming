# SQL - Introduction

This project introduces SQL and MySQL: creating and deleting databases and
tables, inserting, selecting, updating and deleting rows, and using
functions such as `COUNT` and `AVG` with `GROUP BY`.

Run a script with:

    cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

For scripts that use a database, pass its name as an argument:

    cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

| File | Description |
|------|-------------|
| 0-list_databases.sql | Lists all databases |
| 1-create_database_if_missing.sql | Creates the database hbtn_0c_0 |
| 2-remove_database.sql | Deletes the database hbtn_0c_0 |
| 3-list_tables.sql | Lists the tables of a database |
| 4-first_table.sql | Creates the table first_table |
| 5-full_table.sql | Prints the full description of first_table |
| 6-list_values.sql | Lists all rows of first_table |
| 7-insert_value.sql | Inserts a row in first_table |
| 8-count_89.sql | Counts the rows with id = 89 |
| 9-full_creation.sql | Creates second_table and adds rows |
| 10-top_score.sql | Lists records by best score |
| 11-best_score.sql | Lists records with a score >= 10 |
| 12-no_cheating.sql | Updates the score of Bob |
| 13-change_class.sql | Removes records with a score <= 5 |
| 14-average.sql | Computes the score average |
| 15-groups.sql | Counts records by score |
| 16-no_link.sql | Lists records that have a name |

## Requirements
- Ubuntu 20.04 LTS, MySQL 8.0 (8.0.25)
