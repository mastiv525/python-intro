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
    def setUp(self):
        """
        Przygotowanie wspólnych danych testowych:
        - valid_emails: lista poprawnych adresów e-mail
        - invalid_emails: lista niepoprawnych adresów e-mail
        - rectangle_dimensions: krotki (length, width, expected_area)
        - negative_dimensions: wymiary prowadzące do ValueError
        - number_lists: pary (input_list, expected_even_list)
        - date_formats: krotki (input_date, expected_output)
        - invalid_dates: formaty prowadzące do ValueError
        - palindromes: krotki (text, expected_bool)
        """
        self.valid_emails = [
            "user@example.com",
            "first.last@domain.co",
            "a.b-c_xy@sub.domain.org"
        ]
        self.invalid_emails = ["", "user@@example.com", "userexample.com", "user@.com"]

        self.rectangle_dimensions = [
            (3, 4, 12),
            (0, 5, 0),
            (2.5, 4, 10)
        ]
        self.negative_dimensions = [(-1, 5), (5, -2)]

        self.number_lists = [
            ([1, 2, 3, 4], [2, 4]),
            ([], []),
            ([1, 3, 5], [])
        ]

        self.date_formats = [
            ("2025-06-07", "07/06/2025"),
            ("2000-01-01", "01/01/2000")
        ]
        self.invalid_dates = ["07-06-2025", "", "2025/06/07"]

        self.palindromes = [
            ("A man, a plan, a canal: Panama", True),
            ("No lemon, no melon", True),
            ("hello", False),
            ("", True)
        ]

    def test_validate_email(self):
        # Testowanie poprawnych i niepoprawnych adresów e-mail
        for email in self.valid_emails:
            with self.subTest(email=email):
                self.assertTrue(
                    validate_email(email),
                    f"'{email}' powinno być uznane za poprawny email"
                )
        for email in self.invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(
                    validate_email(email),
                    f"'{email}' powinno być uznane za niepoprawny email"
                )

    def test_calculate_rectangle_area(self):
        # Testowanie poprawnych wymiarów prostokąta
        for length, width, expected in self.rectangle_dimensions:
            with self.subTest(length=length, width=width):
                self.assertEqual(
                    calculate_rectangle_area(length, width),
                    expected
                )
        # Testowanie ValueError dla ujemnych wymiarów
        for length, width in self.negative_dimensions:
            with self.subTest(length=length, width=width):
                self.assertRaises(ValueError, calculate_rectangle_area, length, width)

    def test_filter_even_numbers(self):
        # Testowanie filtrowania liczb parzystych z różnych list
        for data, expected in self.number_lists:
            with self.subTest(data=data):
                self.assertEqual(
                    filter_even_numbers(data), expected
                )

    def test_convert_date_format(self):
        # Testowanie konwersji poprawnych formatów daty
        for input_date, expected in self.date_formats:
            with self.subTest(input_date=input_date):
                self.assertEqual(
                    convert_date_format(input_date), expected
                )
        # Testowanie ValueError dla niepoprawnych formatów
        for date_str in self.invalid_dates:
            with self.subTest(date_str=date_str):
                self.assertRaises(ValueError, convert_date_format, date_str)

    def test_is_palindrome(self):
        # Testowanie różnych ciągów tekstowych pod kątem palindromu
        for text, expected in self.palindromes:
            with self.subTest(text=text):
                self.assertEqual(
                    is_palindrome(text), expected
                )

if __name__ == '__main__':
    # Uruchomienie testów: python -m unittest
    import sys
    sys.exit(unittest.main())