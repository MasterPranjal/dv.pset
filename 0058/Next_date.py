#Read the give date as day, month and year

month = int(input("Input the month (e.g. for January(1), February(2) etc.): "))
day = int(input("Input the day: "))
year = int(input("Input the year: "))

days_per_month = 31

if (month == 4 or month == 6 or month == 9 or month == 11):
    days_per_month = 30

elif (month == 2):
    days_per_month = 28
    
elif (year % 4 == 0):
    days_per_month = 29
    
elif (year % 100 == 0):
    days_per_month = 28
    
elif (year % 400 == 0):
    days_per_month = 29

if (day > days_per_month):
    day = 1
    month += 1

if (month >= 12):
      month = 1
      year += 1

print("The date of the next day is: %d/%d/%d", day, month, year)

