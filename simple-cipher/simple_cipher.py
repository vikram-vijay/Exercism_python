from random import choices
from string import ascii_lowercase as letters
from itertools import cycle


class Cipher:
    def __init__(self, key="".join(choices(letters, k=100))):
        self.key = key
        assert self.key.islower(), ValueError("key should be all lower case.")

    @staticmethod
    def _new_text(string, i, j, diff=False):
        if diff:
            return string[(string.index(i) + string.index(j)) % len(string)]
        else:
            return string[(string.index(i) - string.index(j)) % len(string)]

    def encode(self, text):
        return "".join([self._new_text(letters, i, j, True) for i, j in zip(text, cycle(self.key))])

    def decode(self, text):
        return "".join([self._new_text(letters, i, j, False) for i, j in zip(text, cycle(self.key))])
