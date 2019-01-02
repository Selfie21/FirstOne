Days = [ "Monday ", "Tuesday" ,"Wednesday","Thursday","Friday","Saturday","Sunday"]

def whatDay(userMode):

    if userMode == 1:
        strStart = "Hello there traveller!"
    else:
        strStart = "Wazzup bruh!"

    strDate = input(strStart + "\nenter your date in the following format: YYYY \n")
    intYear = int(strDate[0:5])
    finalDay = Days[getStartingDay(intYear)]
    print(finalDay)

def getStartingDay(year):
    thisYear = 2019

    thisYearDay = 1
    factor = 365 % 7
    skipYears = calculatingSkipYears(year, thisYear)

    difYears = thisYear - year
    finalRewind = (thisYearDay - (difYears*factor) - skipYears) % 7

    return finalRewind

def calculatingSkipYears(year, yearNow):
    if year > yearNow:
        return 0
    elif year % 4 == 0:
        return 1
    else:
        while not(yearNow % 4 != 0):
            yearNow = yearNow - 1
        difference = (yearNow - year)/4
        return int(difference)


whatDay(1)