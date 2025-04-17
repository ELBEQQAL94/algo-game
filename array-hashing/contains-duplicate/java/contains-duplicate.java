public static boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> dict = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if(dict.containsKey(nums[i])) {
                Integer currentVal  = dict.get(nums[i]);
                Integer value = currentVal + 1;
                dict.put(nums[i], value);
            } else {
                dict.put(nums[i], 0);
            }
        }

        for (Map.Entry<Integer, Integer> item: dict.entrySet()) {
            Integer value = item.getValue();

            if(value > 0) return true;
        }

        return false;

    }