"""
Moduł math_tools:
Funkcje do podstawowych obliczeń matematycznych.
"""

def factorial(n):
    """
    Oblicza silnię n (n!).
    Args:
        n (int): liczba całkowita >= 0
    Returns:
        int: wynik silni
    Raises:
        ValueError: gdy n < 0 lub nie jest int
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n musi być nieujemną liczbą całkowitą")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    """
    Sprawdza, czy n jest liczbą pierwszą.
    Args:
        n (int): liczba do sprawdzenia
    Returns:
        bool: True jeśli liczba pierwsza, False w przeciwnym razie
    """
    if not isinstance(n, int) or n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True