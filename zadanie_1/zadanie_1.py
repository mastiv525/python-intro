# zadanie1.py

"""
Przykładowy kod demonstrujący:
- zip(): https://docs.python.org/3/library/functions.html#zip
- math.sqrt(): https://docs.python.org/3/library/math.html
- Obsługę wyjątku ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
"""

import math  # Moduł math – dokumentacja: https://docs.python.org/3/library/math.html

def main():
    # Tworzenie dwóch list
    nums = [4, 9, -1, 16]
    labels = ['a', 'b', 'c', 'd']

    # Łączenie list funkcją zip()
    for num, label in zip(nums, labels):  # zip() dokumentacja: https://docs.python.org/3/library/functions.html#zip
        print(f"{label}: {num}")

    # Wykorzystanie math.sqrt() i obsługa wyjątku
    for num in nums:
        try:
            root = math.sqrt(num)
        except ValueError as e:  # ValueError – dokumentacja: https://docs.python.org/3/library/exceptions.html#ValueError
            print(f"Nie można obliczyć pierwiastka z {num}: {e}")
        else:
            print(f"sqrt({num}) = {root}")

if __name__ == "__main__":
    main()
