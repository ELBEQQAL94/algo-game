def twoSum(nums, target):
    p1 = 0
    p2 = p1 + 1
    while p1 < p2 :
        sum = nums[p1] + nums[p2]
        
        if sum == target :
            return [p1 , p2]
        
        p2 = p2 + 1

        if p2 == len(nums):
            p1 = p1 + 1 
            p2 = p1 + 1

nums = [3,3]
target = 6
print(twoSum(nums,target))




