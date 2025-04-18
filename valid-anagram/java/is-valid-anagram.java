public static boolean isAnagram(String s, String t) {
        if (s.length() - t.length() > 0 || s.length() - t.length() < 0) return false;

        HashMap<Character, Integer> hashMapS = fillHashMap(s);
        HashMap<Character, Integer> hashMapT = fillHashMap(t);

        for (HashMap.Entry<Character, Integer> item: hashMapS.entrySet()) {
            Character key = item.getKey();
            Integer value = item.getValue();
            Integer valueT = hashMapT.get(key);
            if (!hashMapT.containsKey(key) || !value.equals(valueT)) {
                return false;
            }
        }

        return true;
    }