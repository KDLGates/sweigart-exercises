def is_valid_date(year:int, month:int, day:int) -> bool:
    
    def is_leap_year(year: int) -> bool:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            return True
        return False
    
    if not month in range(1,13):
        return False
    
    if not day in range(1, 32):
        return False
    
    match month:
        case 2:
            if not is_leap_year(year):
                return day in range(1,29)
            else:
                return day in range(1,30)
        case 4|6|9|11:
            return day in range(1, 31)
        case _:
            return day in range(1, 32)


assert is_valid_date(1999, 12, 31) == True

assert is_valid_date(2000, 2, 29) == True

assert is_valid_date(2001, 2, 29) == False

assert is_valid_date(2029, 13, 1) == False

assert is_valid_date(1000000, 1, 1) == True

assert is_valid_date(2015, 4, 31) == False

assert is_valid_date(1970, 5, 99) == False

assert is_valid_date(1981, 0, 3) == False

assert is_valid_date(1666, 4, 0) == False

 

import datetime

d = datetime.date(1970, 1, 1)

oneDay = datetime.timedelta(days=1)

for i in range(1000000):

    assert is_valid_date(d.year, d.month, d.day) == True

    d += oneDay