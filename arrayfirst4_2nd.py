 
def get_result(nums,end_position):
	for i in range(0,end_position):
		a = nums[i]
		if a == 9:
			return True
	return False

def array_front9(nums):

	if len(nums) < 4:
		return get_result(nums,len(nums))
	else:
		return get_result(nums,4)
  

  # new_list = nums[0:4]
  # new_list = [1,2,0,3]
  # return new_list
  

search9 = array_front9([9])

print(search9)