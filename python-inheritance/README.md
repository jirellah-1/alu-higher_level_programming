# Python - Inheritance

This project covers inheritance in Python 3: listing attributes with
`dir`, checking classes with `type`, `isinstance` and `issubclass`,
subclassing a built-in type, and building a small geometry hierarchy
(`BaseGeometry`, `Rectangle`, `Square`).

| File | Description |
|------|-------------|
| 0-lookup.py | Returns the attributes and methods of an object |
| 1-my_list.py | `MyList`, a list that can print itself sorted |
| 2-is_same_class.py | True if an object is exactly an instance of a class |
| 3-is_kind_of_class.py | True if an object is an instance of a class or a subclass |
| 4-inherits_from.py | True if an object is an instance of a subclass only |
| 5-base_geometry.py | Empty `BaseGeometry` class |
| 6-base_geometry.py | `area()` raises an exception |
| 7-base_geometry.py | Adds `integer_validator` |
| 8-rectangle.py | `Rectangle` based on `BaseGeometry` |
| 9-rectangle.py | Full rectangle with `area()` and `__str__` |
| 10-square.py | `Square` based on `Rectangle` |
| 11-square.py | `Square` with its own description |
| tests/ | Doctest files for tasks 1 and 7 |

## Tests

Run the tests with:

    python3 -m doctest ./tests/*

## Requirements
- Ubuntu 20.04 LTS, python3 (3.8.5)
- pycodestyle 2.7.*
