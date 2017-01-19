# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def isLeap(year):
    if year % 4 != 0 :
        return False
    elif year % 100 == 0 and year % 400 != 0 :
        return False
    else:
        return True

def daysBetweenYears(start,end):
    days_of_year = 0
    if start == end or end - start == 1 :
        return 0
    else:
        initYear = start + 1
        while initYear < end:
            if isLeap(initYear) :
                days_of_year+=366
            else:
                days_of_year+=365
            initYear+=1
    return days_of_year

#def daysTill(day,mon,year):
def daysTill(day,mon):
    days_of_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
#    if isLeap(year):
#	days_of_month[2]=29
    days = 0
    if mon == 1:
        days+=day 
        return days
    else:
        for i in range(mon):
            days+=days_of_month[i]
    return days + day

#def daysAfter(day,mon,year):
def daysAfter(day,mon):
    days = 0
    mon1 = mon
    days_of_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    #print days_of_month
    #if isLeap(year):
#	days_of_month[2] = 29
#	print days_of_month
    if mon == 12 :
        return 31 - day + 1
    else:
        mon+=1
        while mon <= 12 :
            days+= days_of_month[mon]
            mon+=1
        return days+(days_of_month[mon1] - day + 1)
    

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    days_of_year = daysBetweenYears(year1,year2)
    if year1 != year2:
        days_till_day2 = daysTill(day2,month2)
        #days_till_day2 = daysTill(day2,month2,year2)
        days_after_day1 = daysAfter(day1,month1)
        #days_after_day1 = daysAfter(day1,month1,year1)
        tot_days = days_till_day2 + days_after_day1
    else:
        if month2-month1 == 1:
            tot_days = (months[month1-1] - day1 ) + day2
        else:
            tot_days = (months[month1-1] - day1 + 1) + day2 + sum(months[month1:month2 - 1])
    #print days_of_year,tot_days
    return days_of_year + tot_days

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed" #, result, answer
        else:
            print "Test case passed!"

test()
