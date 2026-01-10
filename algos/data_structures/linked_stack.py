import time

from contextlib import contextmanager
from typing import Any, Optional

class Node:
    """Stack node that will be added."""
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional['Node'] = None

class LinkedStack:
    """
    Stack data structure implemented with linked list.

    This class provides the core functionalities of a stack, including push, pop,
    reverse, finding the middle element, and detecting cycles within the structure.
    The stack is implemented as a singly linked list, with constant time complexity
    for operations such as push and pop.

    Methods:
        push: str - adds value to the top of a stack;
        pop: - pops and returns node value;
        reverse_stack: - does a reverse of all node.next links;
        find_middle: - finds middle of a stack, if even numbers returns second;
        is_cycle: - checks if stack nodes are pointing on each another.
    """
    def __init__(self):
        self.top: Optional['Node'] = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        if self._is_empty():
            return 'Stack is empty'

        values = []
        temp_ptr = self.top
        while temp_ptr:
            values.append(str(temp_ptr.value))
            temp_ptr = temp_ptr.next
        return ' -> '.join(values) + ' -> None'


    def _is_empty(self) -> bool | None:
        return self.top is None

    def push(self, value: Any) -> None:
        """Adds value to the top of a stack.

        Complexity:
            O(n)
        """
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self) -> str:
        """Pops/removes node from a top and returns value.

        Complexity:
            O(n)
        """
        if self._is_empty():
            return 'Stack is empty'

        returned_value = self.top.value
        self.top = self.top.next
        self.size -= 1

        return returned_value

    def reverse_stack(self):
        """Reverses the stack in-place.

        Complexity
            O(n)
        """
        prev = None
        curr = self.top
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.top = prev

    def find_middle(self) -> str:
        """Returns the middle element using the Fast/Slow pointer approach."""
        if self._is_empty():
            return 'Stack is empty'
        slow = self.top
        fast = self.top

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.value

    def is_cycle(self) -> bool | str:
        """Detects cycles using Floyd's Cycle-Finding Algorithm."""
        slow = self.top
        fast = self.top

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

@contextmanager
def calculate_time(task_type: str):
    start_time = time.perf_counter()
    try:
        yield
    finally:
        duration = time.perf_counter() - start_time
        print(f'[METRIC] {task_type:<25} | Time: {duration:.8f}s')

stack = LinkedStack()
for i in range(10):
    stack.push(i)

print(stack)

with calculate_time(task_type='Time to pop'):
    stack.pop()
print(stack)

with calculate_time(task_type='Time to reverse'):
    stack.reverse_stack()
print(stack)

with calculate_time(task_type='Time to find middle'):
    stack.find_middle()
print(stack.find_middle())

with calculate_time(task_type='Time to check for cycle'):
    stack.is_cycle()
print(stack.is_cycle())

