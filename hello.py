#x = "This is beautiful"
#print("Hello World "+x)
#mylist = ["suraj","shubham"]
#print(mylist)
#for i in mylist:
#	print(i+" dubey")
mynum = [12,3,4,5,6,7,8] 
def print_odd(xyz):
	print("Odd Value is ",xyz)
#	print_user(xyz)

def print_even(abc):
	print("Even Value is ",abc)
#	print_user2(abc)


def user():
	for num in mynum:
		if num % 2 == 0:
			print_even(num)
		else:
			print_odd(num)
user()


 