import sys
from month import Month

month = int(sys.argv[1])
year = int(sys.argv[2])
cal = Month(month, year)
print cal.display_month()