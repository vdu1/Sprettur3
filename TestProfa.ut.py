# This Python file uses the following encoding: utf-8
from Viktor import Viktor
from Aron import Aron
import unittest
from unittest.mock import patch

class TestProfa(unittest.TestCase):

  def setUp(self):
    self.b=0
    self.Vikt =Viktor()
    self.Ronny =Aron()

  def test_1(self):
    self.assertTrue(True)

  def test_Velja2_returns_s(self):
      self.assertEqual(self.Ronny.Velja2("l"),"s")

  def test_spyrja_returns_true(self ):
      self.assertTrue(self.Vikt.spyrja("Fílar Viktor hávaða? (Já/Nei):", "Nei", 1))

  def test_spyrja_returns_false(self ):
      self.assertFalse(self.Vikt.spyrja("Fílar Viktor hávaða? (Já/Nei):", "Nei", 1))



'''
  def test_spyrja_returns_true(self ):
      self.assertTrue(self.Vikt.spyrja("Fílar Viktor að tala? (Já/Nei):", "Nei", 2))

  def test_spyrja_returns_true(self ):
      self.assertFalse(self.Vikt.spyrja("Fílar Viktor að tala? (Já/Nei):", "Nei", 2))

  def test_spyrja_returns_true(self ):
      self.assertTrue(self.Vikt.spyrja("Elskar Viktor þögnina? (Já/Nei):", "Nei", 3))

  def test_spyrja_returns_true(self ):
      self.assertFalse(self.Vikt.spyrja("Elskar Viktor þögnina? (Já/Nei):", "Já", 3))


  def test_spyrja_returns_true(self ):
      self.assertTrue(self.Vikt.spyrja("Hvað er uppáhaldsdrykkurinn hans Viktors? (Coke Zero/Peru Nocco/Hvítur GoGo/Pepsi Max):", "Pepsi Max", 4))

  def test_spyrja_returns_true(self ):
      self.assertFalse(self.Vikt.spyrja("Hvað er uppáhaldsdrykkurinn hans Viktors? (Coke Zero/Peru Nocco/Hvítur GoGo/Pepsi Max):", "Pepsi Max", 4))

  def test_spyrja_returns_true(self ):
      self.assertTrue(self.Vikt.spyrja("Hvernig bíl á Vikki D? (Trabant/Lada Sport/Audi/Passat)", "Audi", 5))

  def test_spyrja_returns_true(self ):
      self.assertFalse(self.Vikt.spyrja("Hvernig bíl á Vikki D? (Trabant/Lada Sport/Audi/Passat)", "Audi", 5))

  def test_spyrja_returns_true(self ):
      self.assertTrue(self.Vikt.spyrja("Hvað á Viktor margar klippingar eftir? (0/3 max/1/∞):", "3 max", 6))

  def test_spyrja_returns_true(self ):
      self.assertFalse(self.Vikt.spyrja("Hvað á Viktor margar klippingar eftir? (0/3 max/1/∞):", "3 max", 6))

  def test_spyrja_returns_true(self ):
      self.assertTrue(self.Vikt.spyrja("Hvað er uppáhalds tækjavörumerkið hans Viktors? (Apple/Dell/HP/Denver):", "Apple", 7))

  def test_spyrja_returns_true(self ):
      self.assertFalse(self.Vikt.spyrja("Hvað er uppáhalds tækjavörumerkið hans Viktors? (Apple/Dell/HP/Denver):", "Apple", 7))

  def test_spyrja_returns_true(self ):
      self.assertTrue(self.Vikt.spyrja("Hver er besti hópfélagi Viktors? (Hrólfur/Aron/Þorgeir/Víkingur):", "Þorgeir", 8))

  def test_spyrja_returns_true(self ):
      self.assertFalse(self.Vikt.spyrja("Hver er besti hópfélagi Viktors? (Hrólfur/Aron/Þorgeir/Víkingur):", "Þorgeir", 8))

  def test_spyrja_returns_true(self ):
      self.assertTrue(self.Vikt.spyrja("Bjó Vikki D til iPad gryfjuna? (Já/Nei/Ekki Lexi):", "Já", 9))

  def test_spyrja_returns_true(self ):
      self.assertFalse(self.Vikt.spyrja("Bjó Vikki D til iPad gryfjuna? (Já/Nei/Ekki Lexi):", "Já", 9))

  def test_spyrja_returns_true(self ):
      self.assertTrue(self.Vikt.spyrja("Hvað er prófælmyndin hans Viktors gömul? (2 vikna/3 mánaða/6 ára/Á ekki facebook):", "6 ára", 10))

  def test_spyrja_returns_true(self ):
      self.assertFalse(self.Vikt.spyrja("Hvað er prófælmyndin hans Viktors gömul? (2 vikna/3 mánaða/6 ára/Á ekki facebook):", "6 ára", 10))
'''






if __name__ == '__main__':
    unittest.main()
