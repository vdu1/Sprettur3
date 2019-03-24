# This Python file uses the following encoding: utf-8

from Aron import Aron, stor
import unittest
from unittest.mock import patch

class TestAron(unittest.TestCase):

    @patch('Aron.get_input', return_value="12")
    def test_stor_returns_True_when_larger_than_10(self, m):
        self.assertTrue(stor("hversu hátt"))

#    def test_stor_returns_False_when_smaller_than_10(self):
#        self.assertFalse(stor(""))
#
#    def test_stor_returns_False_when_input_is_10(self):
#        self.assertTrue(stor(10))
