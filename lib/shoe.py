#!/usr/bin/env python3

class Shoe:

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Old"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if type(size) in (int, float):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
    pass