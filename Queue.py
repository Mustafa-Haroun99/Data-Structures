import Linked_List


class Queue:
    _linked_list = Linked_List.DoublyLinkedList()

    # Initialize an empty queue
    def __init__(self):
        pass

    # Initialize the queue with an element
    def __int__(self, element):
        self.enqueue(element)

    # Return the size of the queue O(1)
    def size(self):
        return self._linked_list.size()

    # Determine whether the queue is empty or not O(1)
    def is_empty(self):
        return self.size() == 0

    # Return the element in the front of the queue without removing it O(1)
    def head(self):
        if self.is_empty():
            raise Exception("Empty list!")
        else:
            return self._linked_list.get_head()

    # Remove and return the element in the front of the queue O(1)
    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty stack!")
        else:
            return self._linked_list.remove_first()

    # add an element to the end of the queue O(1)
    def enqueue(self, element):
        self._linked_list.add_last(element)

    # Return an iterator of the queue
    def __iter__(self):
        return self._linked_list.__iter__()
