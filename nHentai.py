'''

This program takes as input a 
date and converts the date in-
to a link to a page of nHentai
. I made this program after I  
got an idea when I was bored. 
It took a lot of frustration  
and brain-work but it was wor-
th it. Whenever you wanna read
some hentai but you don't want
to look for one, I guess you  
can use this tool.

Saidkamol Nurjanov
2024

'''

# A function that will check whether the parameter is a leap year
def isLeapYear(checkYear):
    if (checkYear % 4 == 0 and checkYear % 100 != 0) or (checkYear % 400 == 0):
        return True
    return False

# A function that will take as input and validate a date
def inputDate():
    fYear = -1
    while fYear < 0 or fYear > 3000:
        fYear = int(input("Enter a year (must be between 0 and 3000): "))
        if fYear < 0 or fYear > 3000:
            print("You have entered an invalid year.")
    isLeap = isLeapYear(fYear)
    
    fMonth = -1
    while fMonth < 1 or fMonth > 12:
        fMonth = int(input("Enter a month (must be between 1 and 12): "))
        if fMonth < 1 or fMonth > 12:
            print("You have entered an invalid month.")

    fDay = -1
    invalidDay = True
    while invalidDay == True:
        fDay = int(input("Enter a day (depending on the month, must be between 1 and 31): "))
        if (fDay < 1) or (fMonth == [1, 3, 5, 7, 8, 10, 12] and fDay > 31) or (fMonth == [4, 6, 9, 11] and fDay > 30) or (isLeap == False and fMonth == 2 and fDay > 28) or (isLeap == True and fMonth == 2 and fDay > 29):
            print("You have entered an invalid day.")
        else:
            break

    return fYear, fMonth, fDay

# A function that will generate a link
def makeLink(lY, lM, lD):
    link = "https://nhentai.net/g/"
    
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    totalDays = 0
    
    totalDays += int(lY * 365.25)
    for j in range(1, lM):
        totalDays += monthDays[j - 1]
        if j == 2 and isLeapYear(lY):
            totalDays += 1
    totalDays += lD

    link += str(totalDays)
    return link

# MAIN PROGRAM

while True:
    year, month, day = inputDate()
    finalLink = makeLink(year, month, day)
    print("Your link is", finalLink)
    quitProgram = input("Type 0 if you want to quit: ")
    if quitProgram == "0":
        quit()
