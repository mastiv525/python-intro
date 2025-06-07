
# --- app.py ---
"""
Funkcje do lab 2 - Test-Driven Development (TDD)
- validate_email(): https://docs.python.org/3/library/re.html
- calculate_rectangle_area(): proste obliczenia matematyczne
- filter_even_numbers(): operacje na listach
- convert_date_format(): https://docs.python.org/3/library/datetime.html
- is_palindrome(): przetwarzanie ciągów znaków
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
