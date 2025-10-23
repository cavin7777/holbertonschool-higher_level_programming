#!/usr/bin/python3


class CountedIterator:
    def __init__(self, some_iterable):
        self._iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self._iterator)
        self.counter += 1
        return value
