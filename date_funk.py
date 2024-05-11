from datetime import datetime
import calendar

dt = datetime.now()
year = dt.year


def days_in_month(month):
    if month == 2:
        if calendar.isleap(year):
            return 29
        else:
            return 28    
    if month > 7:
        if month % 2 != 0:
            return 30
        else:
            return 31
    if month <= 7:
        if month % 2 != 0:
            return 31
        else:
            return 30    
