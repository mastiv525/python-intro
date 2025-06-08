"""
Moduł text_processing: funkcje do przetwarzania i analizy tekstu.
"""

def word_count(text):
    """
    Zwraca liczbę słów w podanym tekście.
    """
    if not isinstance(text, str):
        raise ValueError("text musi być ciągiem znaków")
    words = text.strip().split()
    return len(words)


def reverse_words(text):
    """
    Odwraca kolejność słów w tekście.
    """
    if not isinstance(text, str):
        raise ValueError("text musi być ciągiem znaków")
    words = text.strip().split()
    return ' '.join(reversed(words))
