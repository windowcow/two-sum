def twoSum(nums: List[int], target: int) -> List[int]:
  # YOUR ANSWER
  hash_table = {}
  
  for index, num in enumerate(nums):
    finding = target - num
    if finding not in hash_table:
      hash_table[num] = index
    else:
      return [hash_table[finding], index]



# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([3, 2, 4], 6))
# print(twoSum([3, 3], 6)) 
