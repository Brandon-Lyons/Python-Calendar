import sys
from month import Month

if len(sys.argv) == 1:
	cal = Month()
else:
	month = int(sys.argv[1])
	year = int(sys.argv[2])
	cal = Month(month, year)
print cal.display_month()