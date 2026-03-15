def is_duplicates(arr: list[int]) -> bool:
    """
        Just need to know if there's a duplicate?
        Use is_duplicates, returns True/False
    """
    seen = set()
    for i in range(len(arr)):
        if arr[i] in seen:
            return True
        seen.add(arr[i])
    return False

def find_dups(arr: list[int]) -> int | None:
    """
        Need to know which number is duplicated?
        Use the fixed find_dups, returns int | None
    """
    unique_nums = set()
    for num in arr:
        if num in unique_nums:
            return num
        unique_nums.add(num)
    return None

def find_dups_v2(arr: list[int]) -> int | None:
    """
        Only if a list consists of int not particularly in sorted order

        Time: O(n)
        Space: O(1)
    """
    slow = 0
    fast = 0

    # Phase 1: Find an intersection point
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    # Phase 2: Find entrance to the cycle
    slow = 0
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow


print(f'{find_dups_v2([1, 2, 3, 4, 4, 5, 6, 7])} is a dup')