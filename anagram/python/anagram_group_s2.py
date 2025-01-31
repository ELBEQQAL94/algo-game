def groupAnagrams(strs):
    result = []
    hashmap = dict()
    for i in range(len(strs)):
        currentValue = strs[i]
        sortedCurrentValue = ''.join(sorted(currentValue))
        if sortedCurrentValue not in hashmap: 
            hashmap[sortedCurrentValue] = [currentValue]
        else:
            group = hashmap[sortedCurrentValue]
            group.append(currentValue)
            hashmap[sortedCurrentValue] = group
          
            
    values = hashmap.values()
    result = list(values)
    return result


strs = ["eat","tea","tan","ate","nat","bat","","" ,"c" ,"c"]
print(groupAnagrams(strs))

            