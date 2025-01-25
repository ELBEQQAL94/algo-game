

def groupAnagrams(strs):
  result = []
  for i in range(len(strs)):
    currentValue = strs[i]
    if check_string(result,currentValue) == False:
        group = [currentValue]
        for j in range(i+1,len(strs)):
            nextValue = strs[j]
            sortedString = ''.join(sorted(currentValue))
            sortedOtherString = ''.join(sorted(nextValue))
            if sortedString == sortedOtherString :
                group.append(nextValue)
        
        result.append(group)
  return result

def check_string(nested_list, target):
    for sublist in nested_list:        
        if target in sublist:            
            return True   
    return False 
    
strs = ["eat","tea","tan","ate","nat","bat"]


print(groupAnagrams(strs))
