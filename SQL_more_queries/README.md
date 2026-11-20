# SQL - More queries

This project goes further with MySQL: creating users and managing their
privileges, constraints (`NOT NULL`, `UNIQUE`, `PRIMARY KEY`,
`FOREIGN KEY`), subqueries, joins, and grouping.

Run a script with:

    cat 0-privileges.sql | mysql -hlocalhost -uroot -p

For scripts that use a database, pass its name as an argument:

    cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa

| File | Description |
|------|-------------|
| 0-privileges.sql | Lists the privileges of user_0d_1 and user_0d_2 |
| 1-create_user.sql | Creates user_0d_1 with all privileges |
| 2-create_read_user.sql | Creates hbtn_0d_2 and a read-only user_0d_2 |
| 3-force_name.sql | Table where name can not be null |
| 4-never_empty.sql | Table where id has a default value |
| 5-unique_id.sql | Table where id is unique |
| 6-states.sql | Database hbtn_0d_usa and the table states |
| 7-cities.sql | The table cities with a foreign key |
| 8-cities_of_california_subquery.sql | Cities of California with a subquery |
| 9-cities_by_state_join.sql | Cities with their state, with a join |
| 10-genre_id_by_show.sql | Shows that have a genre |
| 11-genre_id_all_shows.sql | All shows, with NULL when there is no genre |
| 12-no_genre.sql | Shows without a genre |
| 13-count_shows_by_genre.sql | Number of shows by genre |
| 14-my_genres.sql | Genres of the show Dexter |
| 15-comedy_only.sql | Comedy shows |
| 16-shows_by_genre.sql | Every show with each of its genres |

## Requirements
- Ubuntu 20.04 LTS, MySQL 8.0 (8.0.25)
