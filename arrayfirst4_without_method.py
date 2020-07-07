
def array_front9(nums):

	end_position = 0
	
	if len(nums) <= 4:
		end_position = len(nums)
	else:
		end_position = 4

	for i in range(0,end_position):
		a = nums[i]
		if a == 9:
			return True
	return False

result = array_front9([1,2,3,9,4])
print(result)
