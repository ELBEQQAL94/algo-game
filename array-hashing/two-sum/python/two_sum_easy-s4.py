def twoSum(nums, target):
    hashmap = dict()
    for i , num in enumerate(nums):
        val = target - num
        if val not in hashmap :
           hashmap[num] = i
        else :
           return [hashmap[val],i]
        
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))

