#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        self.first_name = first_name
