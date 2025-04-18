
"""


def containsDuplicate(nums):
    for i in range(len(nums)-1):
        print(nums[i])
        for j in range(i+1 , len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
"""
"""   
def containsDuplicate(nums):
   dictionary_nums = dict()
   for num in nums:
       if num in dictionary_nums:
           print("Key exists!")
           dictionary_nums[num] += 1
       else:
           dictionary_nums[num] = 0
   for num in nums:
       if dictionary_nums[num] > 0:
           return True
   return False
   
"""

def containsDuplicate(nums):
   nums.sort()
   for i in range(len(nums) - 1):
       if nums[i] == nums[i+1]:
           return True
   return False




nums = [1,2,3,5]
print(containsDuplicate(nums))
