def topKFrequent(nums):
    dic =  dict()
    for num in nums:
        if num in dic:
           dic[num] += 1
        else:
            dic[num] = 1

    result = sorted(dic, key=dic.get, reverse=True)[:k] 
    return result

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums))
        