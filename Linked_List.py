class DoublyLinkedList:
    _size = 0
    _head = None
    _tail = None

    # Class of the nodes of the linked list
    class _Node:
        data = None
        prev_node = None
        next_node = None

        def __init__(self, data, prev_node, next_node):
            self.data = data
            self.prev_node = prev_node
            self.next_node = next_node

    # Deleting the linked list O(n)
    def clear(self):
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

    # Return size of the linked list
    def size(self):
        return self._size

    # Determine whether the linked list is empty or not
    def is_empty(self):
        return self.size() == 0

    # Adding element to the tail of the linked list O(1)
    def add_last(self, element):
        if self.is_empty():
            node = self._Node(element, None, None)
            self._head = node
            self._tail = node
        else:
            node = self._Node(element, self._tail, None)
            self._tail.next_node = node
            self._tail = node
        self._size += 1

    # Add element to the beginning of the linked list O(1)
    def add_first(self, element):
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

    # Core insert function
    def _insert(self, element, traversal):
        node = self._Node(element, None, None)
        node.prev_node = traversal
        temporary_node = traversal.next_node
        traversal.next_node = node
        traversal = temporary_node
        node.next_node = traversal
        traversal.prev_node = node

    # Insert element in arbitrary index O(n)
    def insert(self, element, index):
        # Make sure the index is valid
        if index < 0:
            raise Exception("Index out of bounds")

        # If the index is the first or the last index handle these situations independently
        if index == 0:
            self.add_first(element)
        elif index >= self.size():
            self.add_last(element)

        # If the index is elsewhere adjust the pointers of the (index+1)th and the (index-1)th nodes
        else:
            # Search from the head if the index is closer to the beginning of the list
            if index < self.size() / 2:
                traversal = self._head
                for i in range(index-1):
                    traversal = traversal.next_node

            # Search from the tail if the index is closer to the end of the list
            else:
                traversal = self._tail
                for i in range(self.size() - 1, index-1, -1):
                    traversal = traversal.prev_node

            self._insert(element, traversal)
        self._size += 1

    # Return the head of the linked list O(1)
    def get_head(self):
        # Check if the list is empty
        if self.is_empty():
            raise Exception("Empty list!")
        else:
            return self._head.data

    # Return the tail of the linked list O(1)
    def get_tail(self):
        # Check if the list is empty
        if self.is_empty():
            raise Exception("Empty list!")
        else:
            return self._tail.data

    # Remove and return the head of the linked list O(1)
    def remove_first(self):
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

    # Remove and return the tail of the linked list O(1)
    def remove_last(self):
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
                self._tail.next_node = None
        return data

    # Remove arbitrary node of the list O(1)
    def _remove(self, node):
        # If the node is at the beginning or the end of the list handle these situations independently
        if node.next_node is None:
            return self.remove_last()
        if node.prev_node is None:
            return self.remove_first()

        # If the node is elsewhere adjust the next pointer of the previous node and the previous pointer of the next
        # node
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node

        # Extract the value of this node
        data = node.data

        # Reduce the size
        self._size -= 1

        return data

    # Remove node at specific index O(n)
    def remove_at(self, index):
        # Make sure the index is valid
        if index < 0 or index >= self.size():
            raise Exception("Index out of bounds")

        # If the index is the first or the last index handle these situations independently
        if index == 0:
            self.remove_first()
        elif index == self.size()-1:
            self.remove_last()

        # If the index is elsewhere
        else:
            # Search from the head if the index is closer to the beginning of the list
            if index < self.size()/2:
                traversal = self._head
                for i in range(index):
                    traversal = traversal.next_node

            # Search from the tail if the index is closer to the end of the list
            else:
                traversal = self._tail
                for i in range(self.size()-1, index, -1):
                    traversal = traversal.prev_node

            return self._remove(traversal)

    # Remove particular value from the list (it removes the first occurrence of the value) O(n)
    def remove(self, value):
        # Searching for None values
        if value is None:
            traversal = self._head
            while traversal is not None:
                if traversal.data is None:
                    self._remove(traversal)
                    return True
                traversal = traversal.next_node

        # Searching for non-None values
        else:
            traversal = self._head
            while traversal is not None:
                if traversal.data == value:
                    self._remove(traversal)
                    return True
                traversal = traversal.next_node
        raise Exception("There is no such value in the list!")

    # Return the index of particular value in the list (it returns the index of the first occurrence of the value) O(n)
    def index_of(self, value):
        index = 0

        # Searching for None values
        if value is None:
            traversal = self._head
            while traversal is not None:
                if traversal.data is None:
                    return index
                index += 1
                traversal = traversal.next_node

        # Searching for non-None values
        else:
            traversal = self._head
            while traversal is not None:
                if traversal.data == value:
                    return index
                index += 1
                traversal = traversal.next_node

        return -1

    # Check whether the value is contained within the linked list O(n)
    def contains(self, value):
        return self.index_of(value) != -1

    # Define iterator for the list
    def __iter__(self):
        self.current_node = self._head
        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        data = self.current_node.data
        self.current_node = self.current_node.next_node
        return data

    # Convert the linked list to ordinary python list
    def convert_to_list(self):
        return list(iter(self))
