import sys
from month import Month
from year import Year

if len(sys.argv) == 1:
	cal = Month()
elif len(sys.argv) == 2:
	cal = Year(int(sys.argv[1]))
else:
	month = sys.argv[1]
	year = sys.argv[2]
	cal = Month(month, year)
print cal.display()