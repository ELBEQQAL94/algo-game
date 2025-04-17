public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] result = new int[2];

        for (int i = 0 ; i < nums.length; i++) {
            int currentVal = target - nums[i];
            if (map.containsKey(currentVal)) {
                int foundIndexVal = map.get(nums[i]);
                result = new int[]{foundIndexVal, i};
                return result;
            }
            map.put(nums[i], i);
        }
        return result;
    }