#!/usr/bin/python3
"""Unit tests for the Base class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the id counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove files created by the tests."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_auto_ids(self):
        """Ids increment automatically."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)

    def test_given_id(self):
        """A given id is used and does not move the counter."""
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 1)

    def test_id_none(self):
        """An id of None is treated as no id."""
        self.assertEqual(Base(None).id, 1)

    def test_id_other_values(self):
        """Any given value is stored as id."""
        self.assertEqual(Base(-5).id, -5)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base("abc").id, "abc")

    def test_private_counter(self):
        """The counter is a private class attribute."""
        Base()
        self.assertEqual(Base._Base__nb_objects, 1)
        self.assertFalse(hasattr(Base, "__nb_objects"))

    def test_to_json_string_none(self):
        """None gives an empty list string."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """An empty list gives an empty list string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """A list of dicts is converted to a JSON string."""
        res = Base.to_json_string([{"id": 1}])
        self.assertIsInstance(res, str)
        self.assertEqual(res, '[{"id": 1}]')

    def test_to_json_string_two(self):
        """Several dictionaries are converted."""
        d = [{"id": 1, "x": 2}, {"id": 2, "x": 3}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"id": 1, "x": 2}, {"id": 2, "x": 3}]')

    def test_from_json_string_none(self):
        """None gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """An empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_list(self):
        """A JSON string is converted back to a list."""
        res = Base.from_json_string('[{"id": 89, "width": 10}]')
        self.assertIsInstance(res, list)
        self.assertEqual(res, [{"id": 89, "width": 10}])

    def test_json_round_trip(self):
        """to_json_string then from_json_string returns the input."""
        d = [{"id": 1, "width": 2}, {"id": 3, "width": 4}]
        self.assertEqual(
            Base.from_json_string(Base.to_json_string(d)), d)

    def test_save_rectangles(self):
        """save_to_file writes Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(Base.from_json_string(content),
                         [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_squares(self):
        """save_to_file writes Square.json."""
        s1 = Square(5, 0, 0, 1)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(Base.from_json_string(content),
                         [s1.to_dictionary()])

    def test_save_none(self):
        """None saves an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty(self):
        """An empty list saves an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_overwrites(self):
        """An existing file is overwritten."""
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_base_fails(self):
        """Base has no to_dictionary so saving objects fails."""
        with self.assertRaises(AttributeError):
            Base.save_to_file([Base()])

    def test_save_no_args(self):
        """save_to_file needs an argument."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_create_rectangle(self):
        """create returns a Rectangle with the given attributes."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """create returns a Square with the given attributes."""
        s1 = Square(3, 1, 2, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsInstance(s2, Square)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_load_missing_file(self):
        """A missing file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_rectangles(self):
        """Rectangles are loaded back from their file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        out = Rectangle.load_from_file()
        self.assertEqual(len(out), 2)
        for old, new in zip([r1, r2], out):
            self.assertIsInstance(new, Rectangle)
            self.assertIsNot(old, new)
            self.assertEqual(str(old), str(new))

    def test_load_squares(self):
        """Squares are loaded back from their file."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        out = Square.load_from_file()
        self.assertEqual(len(out), 2)
        for old, new in zip([s1, s2], out):
            self.assertIsInstance(new, Square)
            self.assertEqual(str(old), str(new))

    def test_load_empty_file(self):
        """A file with an empty list gives an empty list."""
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
