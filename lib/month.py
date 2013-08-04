class Month(object):

	def __init__(self, month, year):
		self.month = month
		self.year = year

	def header(self):
		month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		string = "%s %s" % (month_names[self.month -1], self.year)
		return string.center(20, ' ').rstrip()

	def week_row(self):
		return "Su Mo Tu We Th Fr Sa"

	def zeller(self):
		m = self.month
		y = self.year
		if self.month == 1 or self.month == 2:
		  m = self.month + 12
		  y = self.year - 1
		first_day = ((1 + (((m + 1) * 26) / 10) + y + (y / 4) + 6 * (y / 100) + (y / 400)) % 7) - 1
		if first_day == -1:
			first_day = 6
		return first_day

