#!/usr/bin/python3
def magic_string():
    magic_string.called = getattr(magic_string, "called", 0) + 1
    return ("BestSchool" + ", BestSchool" * (magic_string.called - 1))
