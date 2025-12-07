def find_min_max(nums: list[int]) -> tuple[int, int]:
    """
    Return (minimum, maximum) from the list.

    Time: O(n) - where n is a number of elements in a list
    Space: O(1) — only a constant number of variables
    """
    largest = nums[0]
    smallest = nums[0]

    for i in range(1, len(nums)):
        if largest < nums[i]:
            largest = nums[i]
        elif smallest > nums[i]:
            smallest = nums[i]
    return smallest, largest

print(find_min_max([2, 34, 1, 0, 23, -6]))