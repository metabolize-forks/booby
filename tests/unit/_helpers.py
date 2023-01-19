# -*- coding: utf-8 -*-

import collections


def stub_validator(value):
    pass


class Spy(object):
    def __init__(self):
        self.times_called = 0

    def __call__(self):
        self.times_called += 1


class MyList(collections.abc.MutableSequence):
    def __init__(self, *args):
        self._store = list(args)

    def __getitem__(self, index):
        return self._store[index]

    def __setitem__(self, index, value):
        pass

    def __delitem__(self, index):
        pass

    def __len__(self):
        pass

    def insert(self, index, value):
        pass


class MyDict(collections.abc.MutableMapping):
    def __init__(self, **kwargs):
        self._store = kwargs

    def __getitem__(self, key):
        return self._store[key]

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        return iter(self._store)
