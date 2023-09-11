#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    char = None if not sentence else sentence[0]
    return length, char
