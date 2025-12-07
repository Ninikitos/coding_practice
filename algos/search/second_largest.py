from typing import Optional

def second_largest(nums: list[int]) -> Optional[int]:
    if len(nums) < 2:
        return None

    largest: Optional[int] = None
    second: Optional[int] = None

    for n in nums:
        # Если ещё нет максимума или нашли новый максимум
        if largest is None or n > largest:
            if largest is not None and n != largest:
                # Старый максимум становится вторым по величине
                second = largest
            largest = n
        # Иначе, если число не равно максимуму и может быть кандидатом на второе место
        elif n != largest and (second is None or n > second):
            second = n

    return second


print(second_largest([2, 2, 2, 2]))

def second_largest_v1(nums: list[int]) -> int:
    if nums[0] > nums[1]:
        largest_one = nums[0]
        largest_two = nums[1]
    else:
        largest_one = nums[1]
        largest_two = nums[0]

    for i in range(2, len(nums)):
        if nums[i] > largest_one:
            largest_two = largest_one
            largest_one = nums[i]
        elif largest_one > nums[i] > largest_two:
            largest_two = nums[i]
    return largest_two

print(second_largest_v1([2, 2, 2, 2]))