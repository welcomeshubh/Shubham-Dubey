# Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.

# if employee is a male and age is in between 20 to 40 then he may work in anywhere

# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

# And any other input of age should print "ERROR".

age = int(input("Enter Age: "))

gender = input("M or F: ")

marital_status = input("Y or N: ")

if gender == "M".lower() and 20 <= age <40:

	print("Can work ANYWHERE.")

elif gender == "M".lower() and 40 <= age < 60:

	print("Can work in URBAN AREAS ONLY.")

elif gender == "F".lower():

	print("Can work only in URBAN AREAS.")

elif age < 20 or age >=60:

	print("ERROR")

else:

	pass