import unittest
from month import Month

class MonthUnitTests(unittest.TestCase):

  def test_header(self):
    cal = Month()
    result = cal.header(5, 2012)
    self.assertEqual("      May 2012", result)

  def test_header_different_month(self):
  	cal = Month()
  	result = cal.header(3, 2012)
  	self.assertEqual("     March 2012", result)