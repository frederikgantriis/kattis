import datetime

async def setDay (x):
    if x == 7:
        x = 1
    else:
        x += 1

async def setDayNumber(x):
    match day:
        case 'MON':
            return 1
        case 'TUE':
            return 2
        case 'WED':
            return 3
        case 'THU':
            return 4
        case 'FRI':
            return 5
        case 'SAT':
            return 6
        case 'SUN':
            return 7

async def setMonth (x):
    match x:
        case 'JAN':
            return 1
        case 'FEB':
            return 2
        case 'MAR':
            return 3
        case 'APR':
            return 4
        case 'MAY':
            return 5
        case 'JUN':
            return 6
        case 'JUL':
            return 7
        case 'AUG':
            return 8
        case 'SEP':
            return 9
        case 'OCT':
            return 10
        case 'NOV':
            return 11
        case 'DEC':
            return 12

date = input().split(' ')

dayNumber = date[0]

monthNumber = 0

monthNumber = setMonth(date[1])

day = input()

dayNumber = setDayNumber(day)


    


today = datetime.date.day()
month = datetime.date.month()

daysInMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
print(today)