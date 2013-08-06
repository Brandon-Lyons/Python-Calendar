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

	def test_number_of_days(self):
		cal = Month(6, 1900)
		self.assertEqual(30, cal.days_number())

	def test_number_of_days_february(self):
		cal = Month(2, 1995)
		self.assertEqual(28, cal.days_number())

	def test_number_of_days_leap_year(self):
		cal = Month(2, 1996)
		self.assertEqual(29, cal.days_number())

	def test_number_of_days_leap_century(self):
		cal = Month(2, 2000)
		self.assertEqual(29, cal.days_number())

	def test_number_of_days_non_leap_century(self):
		cal = Month(2, 1900)
		self.assertEqual(28, cal.days_number())

	def test_blank_spaces(self):
		cal = Month(2, 1990)
		self.assertEqual(["  ","  ","  ","  "], cal.spaces())

	def test_days(self):
		cal = Month(2, 1990)
		expected = [" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"]
		self.assertEqual(expected, cal.days())

	def test_format_days(self):
		cal = Month(2, 1990)
		expected = ["  ","  ","  ","  "," 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"]
		self.assertEqual(expected, cal.format_days())