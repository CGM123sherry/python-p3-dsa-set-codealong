class MySet:

    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def __str__(self):
        set_list = sorted(self.dictionary.keys())  # Sort to match output in the test
        return f'MySet: {{{",".join(map(str, set_list))}}}'  # Converts list to string format

    def add(self, value):
        self.dictionary[value] = True  # Ensures no duplicates, just adds the key
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)  # Removes the value if present, else does nothing
        return self

    def size(self):
        return len(self.dictionary)  # Returns the size of the set (number of keys)

    def clear(self):
        self.dictionary.clear()  # Clears all elements from the set
        return self
