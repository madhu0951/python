year=int(input("enter the year: "))
if year%4==0:
    if year%100==0 and year%400==0:
        print("year is leap year")
    else:
        print("not a leap year")
else:
    print("not a leap year")