# Python program to check if year is a leap year or not
# adapted from www.programiz.com/python-programming/examples/leap-year

year = int(input())
if (year% 4)==0:
   if (year % 100) == 0:
       if (year % 400) == 0:
          print(f"{0}is a leap year")
       else:
           print("{0} isnot a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else: print("{0} is not a leap year".format(year))
