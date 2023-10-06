class Array:
    _length = 0        # The length of the array thought by the user
    _capacity = 0      # Actual length
    _arr = []

    def __init__(self):
        _arr = []

    def __int__(self, capacity):
        if capacity < 0:
            raise Exception("The length of the list can not be less than zero")
        _arr = []
        self._capacity = capacity

    def size(self):
        return self._length

    def is_empty(self):
        return self.size() == 0

    def get(self, index):
        return self._arr[index]

    def set(self, index, value):
        self._arr[index] = value