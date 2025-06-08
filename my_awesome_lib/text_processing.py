"""
Moduł text_processing:
Funkcje do przetwarzania i analizy tekstu.
"""

def word_count(text):
    """
    Zwraca liczbę słów w podanym tekście.
    Args:
        text (str): łańcuch znaków
    Returns:
        int: liczba słów
    Raises:
        ValueError: gdy text nie jest str
    """
    if not isinstance(text, str):
        raise ValueError("text musi być ciągiem znaków")
    words = text.strip().split()
    return len(words)


def reverse_words(text):
    """
    Odwraca kolejność słów w tekście.
    Args:
        text (str): łańcuch znaków
    Returns:
        str: tekst z odwróconą kolejnością słów
    Raises:
        ValueError: gdy text nie jest str
    """
    if not isinstance(text, str):
        raise ValueError("text musi być ciągiem znaków")
    words = text.strip().split()
    return ' '.join(reversed(words))
