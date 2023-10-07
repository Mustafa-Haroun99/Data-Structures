class DoublyLinkedList:
    _size = 0
    _head = None
    _tail = None

    class _Node:                            # Class of the nodes of the linked list
        data = None
        prev_node = None
        next_node = None

        def __init__(self, data, prev_node, next_node):
            self.data = data
            self.prev_node = prev_node
            self.next_node = next_node

    def clear(self):                        # Deleting the linked list
        traversal = self._head
        while traversal is not None:
            next_node = traversal.next_node
            traversal.prev_node = None
            traversal.next_node = None
            traversal.data = None
            traversal = next_node
        self._head = None
        self._tail = None
        traversal = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self.size() == 0