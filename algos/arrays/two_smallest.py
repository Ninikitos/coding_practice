def two_smallest(nums: list[int]) -> tuple[int, int]:
    """
    Return the two smallest distinct values in the list.

    Time: O(n) — one full scan of the list
    Space: O(1) — only constant extra variables
    """
    if nums[0] < nums[1]:
        sm_one, sm_two = nums[0], nums[1]
    else:
        sm_one, sm_two = nums[1], nums[0]

    for i in range(2, len(nums)):
        if nums[i] < sm_one:
            sm_two = sm_one
            sm_one = nums[i]
        elif sm_one < nums[i] < sm_two:
            sm_two = nums[i]

    return sm_one, sm_two

print(two_smallest([2, 4, 1, 5, 0]))
# Output: (0, 1)