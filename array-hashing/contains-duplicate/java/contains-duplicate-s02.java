public static HashMap<Character, Integer> fillHashMap(String s) {
        HashMap<Character, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (hashMap.containsKey(c)) {
                int prevValue = hashMap.get(c);
                int updatedValue = prevValue + 1;
                hashMap.put(c, updatedValue);
            } else {
                hashMap.put(c, 1);
            }
        }

        return hashMap;
    }