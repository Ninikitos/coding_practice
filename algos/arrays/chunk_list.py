def chunk_list(arr: list, size: int) -> list[list] | None:
    """Divide list on sized sub lists

    Time: O(n) - where n is a number of list elements.
    Space: O(n) - where n is a number of list elements.
    """
    if not len(arr): return

    result: list[list] = []
    for i in range(0, len(arr), size):
        result.append(arr[i:i+size])
    return result

print(chunk_list([1,2,3,4,5], 2))