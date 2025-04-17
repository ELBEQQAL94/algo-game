from collections import defaultdict


def groupAnagrams(strs):
    result = []
    hashmap = defaultdict(list)
    for str in strs:
        sortedCurrentValue = ''.join(sorted(str))
        hashmap[sortedCurrentValue].append(str)
                
    values = hashmap.values()
    result = list(values)
    return result


strs = ["eat","tea","tan","ate","nat","bat","","" ,"c" ,"c"]
print(groupAnagrams(strs))

            