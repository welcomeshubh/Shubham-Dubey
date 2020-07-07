
# Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.


# TAKE YEAR INPUT
year = int(input("Enter Year: "))

# CHECK FOR CENTURY YEAR.
if year % 4 == 0 and year % 400 == 0:
	print("{} is CENTURY YEAR.".format(year))

# CHECK FOR LEAP YEAR.
elif year % 4 == 0:
	print("{} is LEAP YEAR.".format(year))

# NOT A LEAP YEAR.
else:
	print("{} is NOT A LEAP YEAR.".format(year))