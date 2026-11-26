# Python - Object-relational mapping

Scripts that connect Python to a MySQL database, first with MySQLdb
(raw SQL), then with SQLAlchemy (an ORM).

## Requirements
- Ubuntu 20.04, Python 3.8, MySQL 8.0
- MySQLdb (mysqlclient) 2.0.x and SQLAlchemy 1.4.x

## Files
- `0-` to `5-`: MySQLdb scripts (select, filter, SQL injection safe, joins)
- `model_state.py`, `model_city.py`: SQLAlchemy models
- `7-` to `14-`: SQLAlchemy scripts (fetch, insert, update, delete)

Usage: `./<script>.py <mysql user> <mysql password> <database> [arg]`
