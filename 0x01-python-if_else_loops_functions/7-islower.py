#!/usr/bin/python3

def islower(c):
    """Checks if the character 'c' is lowercase"""
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False
