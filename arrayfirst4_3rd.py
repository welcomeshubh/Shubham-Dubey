def return_for_length_less_than_4(nums):
	for i in range(0,len(nums)):
		a = nums[i]
		if a == 9:
			return True
	return False
 

def return_for_length_equal_to_more_than_4(nums):
	for i in range(0,4):
		a = nums[i]
		if a == 9:
			return True
	return False

def array_front9(nums):

	if len(nums) < 4:
		return return_for_length_less_than_4(nums)
	else:
		return return_for_length_equal_to_more_than_4(nums)