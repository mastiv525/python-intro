"""
Moduł data_utils:
Funkcje do wczytywania i transformacji struktur danych (list, słowników itp.).
"""

def flatten_list(nested_list):
    """
    Spłaszcza listę zagnieżdżonych list.
    Args:
        nested_list (list of list or items): lista do spłaszczenia
    Returns:
        list: spłaszczona lista
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
    Args:
        seq (iterable): wejściowy ciąg elementów
    Returns:
        list: lista unikalnych elementów
    """
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result