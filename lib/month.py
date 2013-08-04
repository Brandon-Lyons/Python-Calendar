class Month(object):

	def header(self, month, year):
		month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		string = "%s %s" % (month_names[month -1], year)
		return string.center(20, ' ').rstrip()