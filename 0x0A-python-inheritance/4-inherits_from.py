#!/usr/bin/python3
"""
Returns True if the object is an instance of
a class that inherited directly or indirectly
from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of subclass"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
