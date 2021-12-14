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
import inspect
import re
import unittest
import re
import click
import sys

from testing_utils import cli_entry

from orderedtree import orderedtree


class TestCases(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_000_something(self):
        pass


if __name__ == '__main__':
    cli_entry(sys.modules[__name__])()