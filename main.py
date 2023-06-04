from typing import List

def count_adjacent_pairs(arr: List[int]) -> int:
    """
    Подсчитывает количество пар рядом стоящих равных элементов в одномерном массиве.

    Аргументы:
    - arr: Одномерный массив целых чисел.

    Возвращает:
    - Количество пар рядом стоящих равных элементов.
    """
    count = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
    return count


