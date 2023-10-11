import Linked_List


class Stack:
    _linked_list = Linked_List.DoublyLinkedList()

    # Initialize an empty stack
    def __init__(self):
        pass

    # Initialize the stack with an element
    def __int__(self, element):
        self.push(element)

    # Return the size of the stack O(1)
    def size(self):
        return self._linked_list.size()

    # Determine whether the stack is empty or not O(1)
    def is_empty(self):
        return self.size() == 0

    # Push an element to the top of the stack O(1)
    def push(self, element):
        self._linked_list.add_last(element)

    # Pop and return the element in the top of the stack O(1)
    def pop(self):
        if self.is_empty():
            raise Exception("Empty stack!")
        else:
            return self._linked_list.remove_last()

    # Return the element in the top of the stack without removing it O(1)
    def top(self):
        if self.is_empty():
            raise Exception("Empty list!")
        else:
            return self._linked_list.get_tail()

    # Return an iterator of the stack
    def __iter__(self):
        return self._linked_list.__iter__()
