finalStatues = int(input())

def minDaysForStatues(n: int) -> int:
    days = 0
    printer = 1

    while printer < n:
        printer = printer * 2
        days = days + 1
    
    return days+1

print(minDaysForStatues(finalStatues))