import unittest
from month import Month

class MonthUnitTests(unittest.TestCase):

  def test_header(self):
    cal = Month(5, 2012)
    result = cal.header()
    self.assertEqual("      May 2012", result)

  def test_header_different_month(self):
  	cal = Month(3, 2012)
  	result = cal.header()
  	self.assertEqual("     March 2012", result)

  def test_zeller(self):
  	cal = Month(3, 1995)
  	result = cal.zeller()
  	self.assertEqual(3, result)

  def test_zeller_again(self):
    cal = Month(6, 2999)
    self.assertEqual(6, cal.zeller())

  def test_zeller_january(self):
    cal = Month(1, 2000)
    self.assertEqual(6, cal.zeller())

  def test_zeller_february(self):
    cal = Month(2, 2000)
    self.assertEqual(2, cal.zeller())
