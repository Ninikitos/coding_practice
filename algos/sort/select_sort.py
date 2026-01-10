from typing import List

# Version 1
def smallest_num(arr: List[int]) -> int:
    """Return the index of the smallest value in the list."""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort_v1(arr: List[int]) -> list:
    """
    Return a new list containing the elements of ``arr`` in ascending order.

    Time: O(n^2) — find smallest each iteration
    Space: O(n) — result stores all elements
    Note: this version mutates the input list by popping values
    """
    result = []
    for i in range(len(arr)):
        smallest = smallest_num(arr)
        result.append(arr.pop(smallest))
    return result

print(selection_sort_v1([1, 323, 2, 42, 33, 121, 12, 1, 3, 2, 2, 5, 1, 56, 223]))

# Version 2
def selection_sort_v2(arr: List[int]) -> list:
    """
    Return a new list containing the elements of ``arr`` in ascending order in-place.

    Time: O(n^2) — nested loops
    Space: O(n) — result list duplicates storage
    """
    result = []
    for i in range(len(arr)):
        smallest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
        result.append(arr[i])
    return result

print(selection_sort_v2([1, 5, 4, 2]))