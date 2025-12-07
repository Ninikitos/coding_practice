def reverse_slice(nums: list[int], start: int, end: int) -> list[int]:
    """
    Return reversed slice list

    k = end - start (slice length).

    Time:  O(k) - worst case O(n) when k == len(nums)
    Space: O(k) - for the new reversed list
    """
    result = []
    sliced_list = nums[start:end]
    for i in range(len(sliced_list)-1, -1, -1):
        result.append(sliced_list[i])
    return result

print(reverse_slice([1, 2, 3, 4, 5, 6], 0, 6))