public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hashmap = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            String currentVal = strs[i];
            String sortedStr = currentVal
                    .chars()
                    .sorted()
                    .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();

            if (hashmap.containsKey(sortedStr)) {
                List<String> group = hashmap.get(sortedStr);
                group.add(currentVal);
            } else {
                List<String> newGroup = new ArrayList<>();
                newGroup.add(currentVal);
                hashmap.put(sortedStr, newGroup);
            }
        }


        Collection<List<String>> values = hashmap.values();
        List<List<String>> result = new ArrayList<>(values);

        return new ArrayList<>(result);
    }