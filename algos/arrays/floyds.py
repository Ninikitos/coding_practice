arr = [1, 2, 3, 4, 5, 2, 6]
def find_dups(arr: list[int]) -> int | None:
    """
    Find a duplicate in an array where elements are in the range 0 to n-1.

    This function identifies a single duplicate in the provided array using Floyd's
    algorithm. The array must satisfy the condition that
    all elements are integers within the range [0, len(arr) - 1].

    :param arr: List of integers where elements are assumed to be in the range 0 to len(arr) - 1.
    :type arr: list[int]
    :return: The duplicate value if it exists and the input is valid. Returns None when the input
             array doesn't meet the requirements or no duplicate is found.
    :rtype: int | None
    """
    if len(arr) < 2:
        return None

    is_valid = max(arr) <= len(arr) - 1
    if is_valid:
        slow = 0
        fast = 0
        while True:
            slow = arr[slow]
            fast = arr[arr[fast]]
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]
        return slow
    else:
        return None

print(find_dups(arr))



