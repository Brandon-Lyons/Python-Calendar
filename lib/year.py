from month import Month
class Year(object):

  def __init__(self, year):
    self.year = year

  def header(self):
    heading = "%s" %(self.year)
    return heading.center(64, " ").rstrip() + "\n"

  def week_row(self):
    week = "Su Mo Tu We Th Fr Sa"
    return week + "  " + week + "  " + week + "\n"

  def days_array(self, month):
    cal = Month(month, self.year)
    days_array = cal.format_days()
    return days_array

  def month_array(self):
    months = list()
    for i in range(1, 13):
      cal = Month(i, self.year)
      months.append(cal.month_header())
    return months

  def trailing_spaces(self,array):
    n = len(array)
    spaces = list()
    number = 7 - n
    for _ in xrange(number):
      spaces.append("  ")
    return spaces

  def format_3_months(self, a, b, c):
    string = ""
    week1 = list()
    week2 = list()
    week3 = list()
    month1 = self.days_array(a)
    month2 = self.days_array(b)
    month3 = self.days_array(c)
    while month1 or month2 or month3:
      for _ in xrange(7):
        if len(month1) == 0:
          break
        week1.append(month1.pop(0))
      for _ in xrange(7):
        if len(month2) == 0:
          break
        week2.append(month2.pop(0))
      for _ in xrange(7):
        if len(month3) == 0:
          break
        week3.append(month3.pop(0))
      week1.extend(self.trailing_spaces(week1))
      week2.extend(self.trailing_spaces(week2))
      week3.extend(self.trailing_spaces(week3))
      string += (" ".join(week1) + "  ")
      string += (" ".join(week2) + "  ")
      string += (" ".join(week3) + "\n")
      week1 = list()
      week2 = list()
      week3 = list()
    return string

  def display(self):
    string = self.header()
    a = 1 
    b = 2
    c = 3
    for _ in xrange(4):
      string += self.month_array()[a - 1].center(20, " ") + "  "
      string += self.month_array()[b - 1].center(20, " ") + "  "
      string += self.month_array()[c - 1].center(20, " ") + "\n"
      string += self.week_row()
      string += self.format_3_months(a,b,c) + "\n"
      a += 3
      b += 3
      c += 3
    print string