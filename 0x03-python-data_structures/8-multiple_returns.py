#!/usr/bin/python3

"""Returns a tuple with the length if a string and its first character"""


def multiple_returns(sentence):
    if sentence:
        return (len(sentence), sentence[0])
    else:
        return (0, None)
