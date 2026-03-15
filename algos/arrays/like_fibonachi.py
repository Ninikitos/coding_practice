# fib_seq = [1, 2, 6, 8, 14, 22, 36, 58, 94, 152, 246, 398, 644]
def like_fibonacci(first, second):
    """
    Given any two consecutive numbers in a fibonacci-like sequence,
    unwinds backwards to find the two starting numbers that generated it.

    Stops when first > second after subtraction — means we've gone too far back.
    Then swaps back to correct order and returns.
    """
    while first <= second:
        first, second = second - first, first
    first, second = second, first + second
    return first, second

print(like_fibonacci(398, 644))