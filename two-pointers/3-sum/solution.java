class Solution {
   public List<List<Integer>> threeSum(int[] nums){
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        // loop over nums :
        for(int i = 0 ; i < nums.length ; i++)
        {
            int left = i + 1;
            int right = nums.length - 1;
            if(i > 0 && nums[i] == nums[i-1])
                continue;
            while(left < right){

                int total = nums[i] + nums[left] + nums[right];
                if ( total == 0 ){
                    // return here to optimize this code
                    List<Integer> group = new ArrayList<>(Arrays.asList(nums[i],nums[left],nums[right]));
                    result.add(group);
                    // skip duplicates
                    while(left < right && nums[right] == nums[right - 1]) right-- ;
                    while(left < right && nums[left] == nums[left+1]) left++;
                    left++;
                    right--;
                }else if(total < 0){
                    left++;
                }else{
                    right--;
                }

            }

        }

        return result;

    }
}