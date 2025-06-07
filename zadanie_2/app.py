# --- app.py ---
"""
Funkcje dla laboratorium 2 - Test-Driven Development (TDD)
- validate_email(): walidacja adresu e-mail przy użyciu regex (moduł re)
- calculate_rectangle_area(): obliczenie pola prostokąta, obsługa ValueError dla niepoprawnych wymiarów
- filter_even_numbers(): filtracja liczb parzystych z listy
- convert_date_format(): konwersja formatu daty (moduł datetime)
- is_palindrome(): sprawdzenie, czy tekst jest palindromem, ignorowanie niealfanumerycznych znaków
"""
import re
from datetime import datetime


def validate_email(email):  # Walidacja adresu e-mail (regex, moduł re)
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


def calculate_rectangle_area(length, width):  # Obliczenie pola prostokąta
    if length < 0 or width < 0:
        raise ValueError("Długość i szerokość muszą być nieujemne")
    return length * width


def filter_even_numbers(data):  # Filtracja liczb parzystych z listy
    return [x for x in data if isinstance(x, int) and x % 2 == 0]


def convert_date_format(date_str):  # Konwersja formatu daty YYYY-MM-DD na DD/MM/YYYY
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except Exception as e:
        raise ValueError("Data musi mieć format YYYY-MM-DD") from e
    return dt.strftime("%d/%m/%Y")


def is_palindrome(text):  # Sprawdzenie, czy tekst jest palindromem (ignoruje znaki niealfanumeryczne)
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]