def array_front9(nums):
  
  new_list = nums[0:4]
  # new_list = [1,2,0,3]
  # return new_list
  for i in new_list:
    
    if i == 9:
      
      return True
      
  
  return False

search9 = array_front9([])

print(search9)