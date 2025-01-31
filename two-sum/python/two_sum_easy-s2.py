def twoSum(nums, target):
   sorted_nums =  sorted(nums)
   p1 = 0
   p2 = len(sorted_nums) - 1 
   result = []
   counter = 0
   sumOftargetVlues = []
   while p1 < p2 :
     if sorted_nums[p1] + sorted_nums[p2] != target :
        p2 -= 1
     else:
        sumOftargetVlues.append(sorted_nums[p1])
        sumOftargetVlues.append(sorted_nums[p2])

   for i, num in enumerate(nums):
        if num == sumOftargetVlues[counter]:
            counter +=1
            result.append(i)
        if counter == 2:
            break          
   return result


nums = [3,3]
target = 6
print(twoSum(nums, target))
