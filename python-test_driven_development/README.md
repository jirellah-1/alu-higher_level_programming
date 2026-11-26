# Python - Test-driven development

This project covers test-driven development in Python 3: writing the
documentation and the tests first, interactive tests with `doctest`,
and unit tests with `unittest`.

| File | Description |
|------|-------------|
| 0-add_integer.py | Adds two integers or floats |
| 2-matrix_divided.py | Divides all the elements of a matrix |
| 3-say_my_name.py | Prints a first name and a last name |
| 4-print_square.py | Prints a square with the character # |
| 5-text_indentation.py | Prints a text with 2 new lines after . ? and : |
| 6-max_integer.py | Finds the max integer of a list (given) |
| tests/ | The doctest text files and the unittest file |

## Tests

Interactive tests:

    python3 -m doctest ./tests/*

Unit tests:

    python3 -m unittest tests.6-max_integer_test

## Requirements
- Ubuntu 20.04 LTS, python3 (3.8.5)
- pycodestyle 2.7.*
