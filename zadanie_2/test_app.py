

# --- test_app.py ---
import unittest
from app import (
    validate_email,
    calculate_rectangle_area,
    filter_even_numbers,
    convert_date_format,
    is_palindrome
)


class TestApp(unittest.TestCase):
    # Testy dla validate_email
    def test_validate_email_valid(self):
        self.assertTrue(validate_email("test@example.com"))

    def test_validate_email_invalid(self):
        self.assertFalse(validate_email("test@@example.com"))

    def test_validate_email_empty(self):
        self.assertFalse(validate_email(""))

    # Testy dla calculate_rectangle_area
    def test_calculate_rectangle_area_typical(self):
        self.assertEqual(calculate_rectangle_area(3, 4), 12)

    def test_calculate_rectangle_area_zero(self):
        self.assertEqual(calculate_rectangle_area(0, 5), 0)

    def test_calculate_rectangle_area_negative(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-1, 5)

    # Testy dla filter_even_numbers
    def test_filter_even_numbers_typical(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4]), [2, 4])

    def test_filter_even_numbers_empty(self):
        self.assertEqual(filter_even_numbers([]), [])

    def test_filter_even_numbers_all_odd(self):
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])

    # Testy dla convert_date_format
    def test_convert_date_format_typical(self):
        self.assertEqual(convert_date_format("2025-06-07"), "07/06/2025")

    def test_convert_date_format_invalid(self):
        with self.assertRaises(ValueError):
            convert_date_format("07-06-2025")

    def test_convert_date_format_empty(self):
        with self.assertRaises(ValueError):
            convert_date_format("")

    # Testy dla is_palindrome
    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))

    def test_is_palindrome_empty(self):
        self.assertTrue(is_palindrome(""))


if __name__ == '__main__':
    unittest.main()
