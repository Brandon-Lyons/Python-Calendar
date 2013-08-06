class Month(object):

	def __init__(self, month, year):
		self.month = month
		self.year = year

	def header(self):
		month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		string = "%s %s" %(month_names[self.month - 1], self.year)
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

	def days_number(self):
		thirty = [4,6,9,11]
		thirtyone = [1,3,5,7,8,10,12]
		if self.month in thirty:
			return 30
		elif self.month in thirtyone:
			return 31
		elif self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0):
			return 29
		else:
			return 28

	def spaces(self):
		spaces = list()
		for _ in xrange(self.zeller()):
			spaces.append("  ")
		return spaces

	def days(self):
		days = list()
		for i in range(1,self.days_number() + 1):
			num = str(i)
			if len(num) == 1:
				num = " " + num
				days.append(num)
			else:
				days.append(num)
		return days

	def format_days(self):
		formatted = list()
		formatted.extend(self.spaces())
		formatted.extend(self.days())
		return formatted

	def display_month(self):
		header = self.header() + "\n" + self.week_row() + "\n"
		days = self.format_days()
		weeks = ""
		while days:
			for _ in xrange(7):
				weeks += days.pop(0) + " "
				if len(days) == 0:
					break
			weeks += "\n"
		month = header + weeks
		return month