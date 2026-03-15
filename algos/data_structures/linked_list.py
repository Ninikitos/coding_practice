class Node:
    """
   A single element in a LinkedList.
   Holds a value and a pointer to the next node.
   Think of it like a train car it has cargo (value) and
   is connected to the next car (next).

    Node(1) -> Node(2) -> Node(3) -> None
   """
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    """
    A chain of Nodes where each node points to the next one.
    Unlike a regular list, elements are NOT stored in contiguous memory
    each node can be anywhere, connected only by pointers.

    Regular list:  [1, 2, 3, 4]     - index access is instant O(1)
    Linked list:   1 -> 2 -> 3 -> 4 - must walk from head O(n)

    Good at:
        inserting/removing at the start → O(1), just update head
        inserting/removing in the middle → O(n), must walk to the spot
    Bad at:
        random access → no indexes, must walk from head every time
    """
    def __init__(self, value):
        """Creates a new LinkedList with a single node as the head."""
        self.head = Node(value)
        self.tail = self.head
        self.size = 0

    def __len__(self):
        """Lets you call len(linked_list) just like a regular list."""
        return self.size

    def __str__(self):
        """
        Pretty prints the list so you can actually see the chain.
        head → 1 -> 2 -> 3 -> None
        """
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        return ' -> '.join(values) + ' -> ' + 'None'

    def get_at_index(self, index):
        """
        Returns the value at the given index, or None if index is out of range.
        Always walks from head, O(n).

        Why return None instead of raising an error:
            return None      - caller decides what to do, silent
            raise IndexError - loud, forces caller to handle it
        """
        if index < 0 or index >= self.size:
            print(f'Index {index} is out of range, list size is {self.size}')
            return None
        curr = self.head
        counter = 0
        while counter < index:
            curr = curr.next
            counter += 1
        return curr.value

    def push_to_end(self, value):
        """
        Adds a new node at the end of the list -> O(1) thanks to tail pointer.
        No walking needed - tail always knows where the last node is.
        """
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def push_to_start(self, value):
        """
        Adds a new node at the start of the list -> O(1), no walking needed.
        Just rewires head to point to the new node.

        Tail only updates when the list was empty before inserting
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.size == 0:
            self.tail = self.head
        self.size += 1

    def push_to_index(self, *, value, index):
        """
        Inserts a new node at the given index.
        Walks to index-1, then rewires pointers around the new node.
        """
        if index < 0 or index > self.size:
            print(f'Index {index} is out of range, list size is {self.size}')
            return None

        if index == 0:
            self.push_to_start(value)
            return None

        if index == self.size:
            self.push_to_end(value)
            return None

        new_node = Node(value)
        curr = self.head
        counter = 0
        while counter < index - 1:
            curr = curr.next
            counter += 1
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1
        return None

    def remove_head(self):
        """
        Removes the first node from the list -? O(1), no walking needed.
        Just moves head forward by one. If there is no head, tail becomes None.
        """
        if self.head is None:
            print('List is empty')
            return None

        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.tail = None
        return None

    def remove_tail(self):
        """
        Removes the last node from the list -> O(n), must walk to second-to-last.
        Updates tail to keep the tail pointer accurate.
        """
        if self.head is None:
            print('List is empty')
            return None

        if self.head.next is None:
            self.head = None
            self.tail = None
            self.size = 0

        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
        self.tail = curr
        self.size -= 1
        return None

    def remove_at_index(self, index):
        """
        Removes the node at the given index.
        Walks to index-1, then skips over the target node.
        """
        if self.head is None:
            print('List is empty')
            return None

        if index < 0 or index >= self.size:
            print(f'Index {index} is out of range, list size is {self.size}')
            return None

        if index == 0:
            return self.remove_head()

        curr = self.head
        counter = 1
        while counter < index:
            curr = curr.next
            counter += 1

        next_node = curr.next.next
        curr.next = next_node

        if next_node is None:
            self.tail = curr

        self.size -= 1
        return None

    def reverse(self):
        """
        Reverses the list in place by flipping all pointers -> O(n).
        Uses three pointers: prev, curr, next_node to rewire one node at a time.
        """
        if self.head is None:
            print('List is empty')
            return None

        old_head = self.head

        curr = self.head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev
        self.tail = old_head
        return None

    def is_value(self, value):
        """
        Checks if a value exists anywhere in the list.
        Returns True if found, False if not -> O(n), must walk the whole list.
        """
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def copy_list(self):
        """
        Creates a brand new LinkedList with the same values → O(n).
        Deep copy — changing one list won't affect the other.
        """
        if self.head is None:
            print('List is empty, nothing to copy')
            return

        curr = self.head
        new_list = LinkedList(curr.value)
        curr = curr.next
        while curr:
            new_list.push_to_end(curr.value)
            curr = curr.next
        return new_list

l = LinkedList(1)
for i in range(2, 20):
    l.push_to_end(i)

print(f'Linked list len: {len(l)}')
print(l)
l.reverse()
print(l)
