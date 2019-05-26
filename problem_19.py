# -*- coding: utf-8; -*-


import calendar

# Number of days per month (except for February in leap years)
from collections import OrderedDict
from itertools import cycle

mdays = OrderedDict(
    (("Jan", 31), ("Feb", 28), ("Mar", 31), ("April", 30), ("May", 31),
     ("June", 30),
     ("Jul", 31), ("Aug", 31), ("Sep", 30), ("Oct", 31), ("Nov", 30),
     ("Dec", 31)))

day = cycle(["Mon", "Ths", "Wes", "Thr", "Fri", "Sat", "Sun"])


def isleap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main():
    result = list()
    for year in range(1900, 2001):
        for month, n in mdays.items():
            if month == "Feb" and isleap(year):
                n = 29
            for d in range(1, n + 1):
                cday = next(day)
                cdate = "%s %d %s %s" % (cday, d, month, year)
                print(cdate)
                if cday == "Sun" and d == 1 and year >= 1901:
                    result.append(cdate)
    return result


if __name__ == '__main__':
    print(len(main()))
