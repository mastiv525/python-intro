"""
Moduł data_utils: funkcje do wczytywania i transformacji struktur danych.
"""

def flatten_list(nested_list):
    """
    Spłaszcza listę zagnieżdżonych list.
    """
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.extend(element)
        else:
            result.append(element)
    return result


def unique_items(seq):
    """
    Zwraca unikalne elementy zachowując kolejność.
    """
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
