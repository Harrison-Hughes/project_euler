# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


def how_many_sundays(start_year, end_year, start_day):
    non_leap_month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_month_lengths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    [sunday_counter, start_of_month] = [0, start_day]
    for year in range(start_year, end_year+1):
        months = []
        if ((not year % 100 == 0) and year % 4 == 0) or (year % 400 == 0):
            for month in range(12):
                # print(year, month, start_of_month)
                if start_of_month == 0:
                    sunday_counter += 1
                    months.append(month)
                start_of_month = (
                    start_of_month + leap_month_lengths[month]) % 7
        else:
            for month in range(12):
                # print(year, month, start_of_month)
                if start_of_month == 0:
                    sunday_counter += 1
                    months.append(month)
                start_of_month = (
                    start_of_month + non_leap_month_lengths[month]) % 7
        print(year, months)
    return sunday_counter


if __name__ == "__main__":
    print(how_many_sundays(1901, 2000, 2))
