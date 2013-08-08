import unittest
from year import Year

class YearUnitTests(unittest.TestCase):

  def test_header(self):
    cal = Year(2012)
    self.assertEqual("                              2012\n", cal.header())

  def test_week_row(self):
    cal = Year(2012)
    expected = "Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa\n"
    self.assertEqual(expected, cal.week_row())

  def test_days_array(self):
    cal = Year(2012)
    expected = [" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
    self.assertEqual(expected, cal.days_array(1))

  def test_month_array(self):
    cal = Year(2012)
    expected = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    self.assertEqual(expected, cal.month_array())

  def test_3_months(self):
    cal = Year(2012)
    expected = """ 1  2  3  4  5  6  7            1  2  3  4               1  2  3
 8  9 10 11 12 13 14   5  6  7  8  9 10 11   4  5  6  7  8  9 10
15 16 17 18 19 20 21  12 13 14 15 16 17 18  11 12 13 14 15 16 17
22 23 24 25 26 27 28  19 20 21 22 23 24 25  18 19 20 21 22 23 24
29 30 31              26 27 28 29           25 26 27 28 29 30 31
"""
    self.assertEqual(expected, cal.format_3_months(1,2,3))