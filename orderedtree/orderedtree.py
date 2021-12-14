#!/usr/bin/env python
# coding=utf-8
"""
# orderedtree : An ordered tree with arbitrary ordering ability

Summary :
    A binary ordered tree which applies ordering on inserts and removal. Will support iteration and indexing (eventually)

Use Case :
    I want a list type object which is ordered and stays ordered

Testable Statements :
    ...
"""

from . version import *


class _Node:
    def __init__(self, data, key_cache):
        self._data = data
        self._key_cached = key_cache
        self._parent = None
        self._left_children = None
        self._right_children = None
        self._count_left_children = 0
        self._count_right_children = 0

    def __len__(self):
        """The Length of this node and it's children"""
        return self._count_right_children +self._count_left_children +1


class OrderedTree:
    """An container implemented as a Tree that is automatically kept in a given sort order based on a key function
    The default ordering is the default Python comparison operator
    """
    def __init__(self, initial=None, *, key=None):
        """
        :param initial: An initial iterator to be added to the tree
        :param key: A key function used to order the tree.
        """
        self._tree = None
        self._key_func = key

    def __len__(self):
        return len(self._tree) if self._tree else 0