class Solution {
    public boolean isPalindrome(String s) {
        String new_string = s.replaceAll("[^a-zA-Z0-9]","").toLowerCase();
        int left = 0;
        int right = new_string.length() - 1;
        
        while (left < right) {
            if (new_string.charAt(left) != new_string.charAt(right)) {
                return false;
            }
            
            left += 1;
            right -= 1;
        }
        
        return true;
    }
}