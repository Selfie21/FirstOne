from enum import Enum





whatDay(1)

def getStartingDay(year):
    thisYear = 2019

    thisYearDay = 1
    factor = 365 % 7
    skipYears = calculatingSkipYears(year, thisYear)
    rewindYear =  ((thisYearDay - ((thisYear - year) * factor)) + skipYears) % 7

def whatDay(userMode):

    if userMode == 1:
        strStart = "Hello there traveller!"
    else:
        strStart = "Wazzup bruh!"


    strDate = input("enter your date in the following format: DD/MM/YYYY \n")
    intDay = int(strDate[0:2])
    intMonth = int(strDate[3:5])
    intYear = int(strDate[6:10])


    print(strStart + strFinal)

def calculatingSkipYears(year, yearNow):
    if (yearNow-year) < 4 and year > yearNow:
        return 0
    else:
        while not(yearNow % 4 != 0):
            yearNow = yearNow - 1
        difference = (yearNow - year)/4
        return int(difference)

