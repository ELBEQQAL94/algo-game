public static int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int currentVal = nums[i];
            if (hashmap.containsKey(currentVal)) {
                int prevCounter = hashmap.get(currentVal);
                int newCounter = prevCounter + 1;
                hashmap.put(currentVal, newCounter);
            } else {
                hashmap.put(currentVal, 1);
            }
        }


        int[] result = hashmap
                .entrySet()
                .stream()
                .sorted(Map.Entry.<Integer, Integer>comparingByValue().reversed())
                .limit(k)
                .mapToInt(Map.Entry::getKey)
                .toArray();

        return result;
    }