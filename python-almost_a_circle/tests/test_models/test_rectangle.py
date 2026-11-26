#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Reset the id counter before each test."""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """Rectangle is a Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_ids(self):
        """Ids are automatic unless given."""
        self.assertEqual(Rectangle(1, 2).id, 1)
        self.assertEqual(Rectangle(1, 2).id, 2)
        self.assertEqual(Rectangle(1, 2, 0, 0, 12).id, 12)

    def test_attributes(self):
        """All attributes are stored."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 3, 4, 5))

    def test_defaults(self):
        """x and y default to 0."""
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_private_attributes(self):
        """Attributes are private with getters and setters."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r._Rectangle__width, 1)
        self.assertEqual(r._Rectangle__height, 2)
        self.assertEqual(r._Rectangle__x, 3)
        self.assertEqual(r._Rectangle__y, 4)

    def test_setters(self):
        """Setters change valid values."""
        r = Rectangle(1, 2)
        r.width = 5
        r.height = 6
        r.x = 7
        r.y = 8
        self.assertEqual((r.width, r.height, r.x, r.y), (5, 6, 7, 8))

    def test_missing_args(self):
        """width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        """Too many arguments are refused."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_type_errors(self):
        """Non-integers raise TypeError with the right message."""
        bad = ["2", 2.5, None, True, [1], {}, (1,), {1}]
        for value in bad:
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                        TypeError, "^width must be an integer$"):
                    Rectangle(value, 1)
                with self.assertRaisesRegex(
                        TypeError, "^height must be an integer$"):
                    Rectangle(1, value)
                with self.assertRaisesRegex(
                        TypeError, "^x must be an integer$"):
                    Rectangle(1, 1, value)
                with self.assertRaisesRegex(
                        TypeError, "^y must be an integer$"):
                    Rectangle(1, 1, 1, value)

    def test_type_errors_setters(self):
        """Setters also validate types."""
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = "1"
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.height = 1.5
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.y = None

    def test_value_errors_size(self):
        """width and height must be > 0."""
        for value in (0, -1, -100):
            with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
                Rectangle(value, 1)
            with self.assertRaisesRegex(ValueError, "^height must be > 0$"):
                Rectangle(1, value)

    def test_value_errors_position(self):
        """x and y must be >= 0."""
        with self.assertRaisesRegex(ValueError, "^x must be >= 0$"):
            Rectangle(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "^y must be >= 0$"):
            Rectangle(1, 1, 0, -1)

    def test_value_errors_setters(self):
        """Setters also validate values."""
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = 0
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.x = -1
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.y = -1

    def test_zero_position_ok(self):
        """0 is valid for x and y."""
        r = Rectangle(1, 1, 0, 0)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_validation_order(self):
        """width is validated before height."""
        with self.assertRaisesRegex(TypeError, "width"):
            Rectangle("a", "b")

    def test_area(self):
        """area returns width * height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_big(self):
        """area works with large numbers."""
        self.assertEqual(Rectangle(999999999, 999999999).area(),
                         999999998000000001)

    def test_area_args(self):
        """area takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).area(1)

    def test_display_basic(self):
        """display prints the rectangle with #."""
        with patch("sys.stdout", new=StringIO()) as out:
            Rectangle(4, 2).display()
        self.assertEqual(out.getvalue(), "####\n####\n")

    def test_display_small(self):
        """display works for a 1x1 rectangle."""
        with patch("sys.stdout", new=StringIO()) as out:
            Rectangle(1, 1).display()
        self.assertEqual(out.getvalue(), "#\n")

    def test_display_xy(self):
        """display uses x and y offsets."""
        with patch("sys.stdout", new=StringIO()) as out:
            Rectangle(2, 3, 2, 2).display()
        self.assertEqual(out.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_display_x_only(self):
        """display uses the x offset."""
        with patch("sys.stdout", new=StringIO()) as out:
            Rectangle(3, 2, 1, 0).display()
        self.assertEqual(out.getvalue(), " ###\n ###\n")

    def test_display_y_only(self):
        """display uses the y offset."""
        with patch("sys.stdout", new=StringIO()) as out:
            Rectangle(1, 1, 0, 2).display()
        self.assertEqual(out.getvalue(), "\n\n#\n")

    def test_str(self):
        """__str__ has the right format."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        """update with positional arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_extra_args(self):
        """Extra positional arguments are ignored."""
        r = Rectangle(1, 1)
        r.update(5, 2, 3, 4, 5, 6, 7)
        self.assertEqual(str(r), "[Rectangle] (5) 4/5 - 2/3")

    def test_update_kwargs(self):
        """update with keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_args_beat_kwargs(self):
        """kwargs are skipped when args exist."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, width=50)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_unknown_key(self):
        """Unknown keys are ignored."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(foo=3)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_update_no_args(self):
        """update with nothing changes nothing."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_validation(self):
        """update validates through the setters."""
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.update(1, "a")
        with self.assertRaises(ValueError):
            r.update(width=-1)

    def test_to_dictionary(self):
        """to_dictionary returns all attributes."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {"id": 1, "width": 10, "height": 2,
                             "x": 1, "y": 9})

    def test_to_dictionary_update(self):
        """A dictionary can be passed back to update."""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_to_dictionary_copy(self):
        """Changing the dictionary does not change the object."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.to_dictionary()["width"] = 99
        self.assertEqual(r.width, 1)


if __name__ == "__main__":
    unittest.main()
