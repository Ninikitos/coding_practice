from typing import Iterable, Any


def my_zip(a: Iterable[Any], b: Iterable[Any]) -> list[tuple]:
    """
    Reimplementation of built-in zip for two iterables.

    Time: O(k) - k is the number of pairs (length of the shortest iterable)
    Space: O(k) - k is the number of pairs (length of the shortest iterable)
    """
    zip()
    try:
        it_a = iter(a)
    except TypeError:
        raise TypeError("First argument is not iterable")

    try:
        it_b = iter(b)
    except TypeError:
        raise TypeError("Second argument is not iterable")

    result: list[tuple] = []
    while True:
        try:
            va = next(it_a)
            vb = next(it_b)
        except StopIteration:
            break
        result.append((va, vb))
    return result