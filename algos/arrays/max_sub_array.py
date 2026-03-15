def max_sum_subarray(nums: list[int], k: int) -> int:
    """
    Finds the maximum sum of any contiguous subarray of size k.
    Uses the sliding window technique - slides a window of size k across
    the array, updating the sum by dropping the left element and adding
    the new right element instead of recalculating from scratch each time.

    Visual on [2, 1, 5, 1, 3, 2], k=3:
        [2, 1, 5] 1, 3, 2  → sum = 8
         2, [1, 5, 1] 3, 2 → sum = 7   (dropped 2, added 1)
         2, 1, [5, 1, 3] 2 → sum = 9   (dropped 1, added 3) ← max
         2, 1, 5, [1, 3, 2]→ sum = 6   (dropped 5, added 2)
        return 9

    The slide formula:
        current_sum = current_sum + nums[i] - nums[i - k]

    Edge cases:
        max_sum_subarray([1, 2], 5)   # → 0  k larger than array, can't fit a window
        max_sum_subarray([5], 1)      # → 5  single element, window = whole array

    Why not recalculate every window from scratch:
        brute force  → sum every window of k elements → O(n*k) gets slow fast
        sliding window → one add, one subtract per step → O(n) always fast

        nums = list(range(1_000_000))
        max_sum_subarray(nums, 1000)  # sliding window handles this fine
                                      # brute force would do 1 billion operations
        """
    if len(nums) < k:
        return 0
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(k, len(nums)):
        current_sum = current_sum + nums[i] - nums[i - k]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3)) # 9
print(max_sum_subarray([2, 3, 4, 1, 5], 2))    # 7