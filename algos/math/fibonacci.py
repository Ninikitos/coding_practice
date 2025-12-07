from typing import List

def fibonacci_list_v1(n: int) -> List[int]:
    """
    Return first n Fibonacci numbers as a list (0-indexed sequence).

    Time: O(n) - where n is a number of sequences that will be calculated.
    Space: O(n) - where n is a number of sequences that will be calculated.
    """
    if n == 0:
        return []
    if n == 1:
        return [0]

    result = [0, 1]

    for _ in range(2, n):
        result.append(result[-1] + result[-2])
    return result


def fibonacci_list_v2(n: int) -> List[int]:
    """
    Return first n Fibonacci numbers as a list (0-indexed sequence).

    Time: O(n) - where n is a number of sequences that will be calculated.
    Space: O(n) - where n is a number of sequences that will be calculated.
    """
    a = 0
    b = 1

    result = [0]

    for _ in range(1, n):
        temp = a + b
        b = a
        a = temp
        result.append(temp)
    return result

if __name__ == "__main__":
    print(fibonacci_list_v1(3))  # [0, 1, 1]
    print(fibonacci_list_v2(3))  # [0, 1, 1]


