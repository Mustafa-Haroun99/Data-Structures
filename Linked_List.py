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

    def clear(self):                        # Deleting the linked list O(n)
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

    def size(self):                         # Return size of the linked list
        return self._size

    def is_empty(self):                     # Determine whether the linked list is empty or not
        return self.size() == 0

    def add_last(self, element):            # Adding element to the tail of the linked list O(1)
        if self.is_empty():
            node = self._Node(element, None, None)
            self._head = node
            self._tail = node
        else:
            node = self._Node(element, self._tail, None)
            self._tail.next_node = node
            self._tail = node
        self._size += 1

    def add_first(self, element):           # Adding element to the beginning of the linked list O(1)
        # Check if the list is empty
        if self.is_empty():
            node = self._Node(element, None, None)
            self._head = node
            self._tail = node
        else:
            node = self._Node(element, None, self._head)
            self._head.prev_node = node
            self._head = node
        self._size += 1

    def add(self, element):                 # Adding element to the tail of the linked list O(1)
        self.addLast(element)

    def get_head(self):                     # Return the head of the linked list O(1)
        # Check if the list is empty
        if self.is_empty():
            raise Exception("Empty list!")
        else:
            return self._head.data

    def get_tail(self):                     # Return the tail of the linked list O(1)
        # Check if the list is empty
        if self.is_empty():
            raise Exception("Empty list!")
        else:
            return self._tail.data

    def remove_first(self):                 # Remove and return the head of the linked list O(1)
        # Check if the list is empty
        if self.is_empty():
            raise Exception("Empty list!")
        else:
            # Extract the data at the head
            data = self._head.data

            # Forward the head pointer by one
            self._head = self._head.next_node

            # Reduce the size of the list by one
            self._size -= 1

            # If the list is now empty make the tail to be None
            if self.is_empty():
                self._tail = None

            # If it is not empty just clear the previous pointer of the head
            else:
                self._head.prev_node = None
        return data

    def remove_last(self):                 # Remove and return the tail of the linked list O(1)
        # Check if the list is empty
        if self.is_empty():
            raise Exception("Empty list!")
        else:
            # Extract the data at the tail
            data = self._tail.data

            # backward the tail pointer by one
            self._tail = self._tail.prev_node

            # Reduce the size of the list by one
            self._size -= 1

            # If the list is now empty make the head to be None
            if self.is_empty():
                self._head = None

            # If it is not empty just clear the next pointer of the tail
            else:
                self._head.next_node = None
        return data

    def _remove(self, node):                 # Remove arbitrary node of the list
        # If the node is at the beginning or the end of the list handle these situations independently
        if node.next is None:
            return self.remove_last()
        if node.prev is None:
            return self.remove_first()

        # If the node is elsewhere adjust the next pointer of the previous node and the previous pointer of the next
        # node
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node

        # Extract the value of this node
        data = node.data

        # Reduce the size
        self.size -= 1

        return data

    def remove_at(self, index):
        # Make sure the index is valid
        if index < 0 or index >= self.size():
            raise Exception("Index out of bounds")

        # Search from the head if the index is closest to the closest to the beginning of the list
        if index < self.size()/2:
            traversal = self._head
            for i in range(index):
                traversal = traversal.next_node

        # Search from the tail if the index is closest to the closest to the end of the list
        else:
            traversal = self._tail
            for i in range(self.size()-1, index, -1):
                traversal = traversal.prev_node

        return self._remove(traversal)





lin = DoublyLinkedList()
lin.add_last(3)
lin.add_last(3)
lin.add_last(4)
lin.clear()
print(lin.size())