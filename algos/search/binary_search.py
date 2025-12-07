from typing import List

def binary_search(nums: List[int], target: int) -> int:
    """
    Return index or -1 if not found.

    Time: O(log n) - n is a number of elements in a list;
    Space: O(1) - only a few variables are used regardless of input size.
    """
    left = 0
    right = len(nums) - 1
    step = 0
    while left <= right:
        mid = (left + right) // 2
        step += 1
        if target == nums[mid]:
            print(f'Found in {step} steps')
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    print(binary_search([1,3,5,7,9], 1))
