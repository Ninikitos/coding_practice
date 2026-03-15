def move_zeros(arr: list[int]) -> list:
    """
        Moves all zeros in a list to the end, keeping non-zero numbers in their original order.
        Does this IN-PLACE (modifies the original list, doesn't create a new one).

        Uses the "two pointer" technique — a classic pattern where two variables
        (slow and fast) crawl through the list at different speeds:

            - fast - scans every single element one by one
            - slow - only moves forward when it places a non-zero number

        How it works step by step on [1, 0, 3]:
            fast=0 - arr[0]=1, not zero - swap arr[0] with arr[0], slow=1
            fast=1 - arr[1]=0, it's zero - do nothing, slow stays at 1
            fast=2 - arr[2]=3, not zero - swap arr[1] with arr[2] - [1, 3, 0], slow=2
            result - [1, 3, 0]

        Edge cases:
            move_zeros([0, 0, 0])    # - [0, 0, 0]  (all zeros, nothing moves)
            move_zeros([1, 2, 3])    # - [1, 2, 3]  (no zeros, nothing changes)
            move_zeros([])           # - []          (empty list, no problem)

        Why not just do: [x for x in arr if x != 0], [0] * count_of_zeros?
            That creates a brand new list and uses extra memory.
            The two-pointer approach does it with O(1) extra space no new list,
            just swapping elements in place. Useful when memory is tight or the
            list is huge.
        """
    # no_zeros = [x for x in arr if x != 0]
    # zero_count = len(arr) - len(no_zeros)
    # return no_zeros + [0] * zero_count

    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
    return arr

arr = [1, 2, 0, 4, 51, 123, 0, 123, 0, 0, 43, 1, 0]
print(move_zeros(arr))