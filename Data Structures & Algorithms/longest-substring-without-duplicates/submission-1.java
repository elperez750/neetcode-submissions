class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int maxLength = 0;
        int left = 0;
        int right = 1;
        if (s.length() == 0) return 0;
        // Adding first character
        set.add(s.charAt(left));

        while (right < s.length()) {
            if (set.contains(s.charAt(right))) {
                int ssLength = right - left;
                System.out.println(ssLength);

                if (ssLength > maxLength) {
                    maxLength = ssLength;
                }
                while (set.contains(s.charAt(right))) {
                    set.remove(s.charAt(left));
                    left++;
                }
                
            }

         
                set.add(s.charAt(right));

            


            System.out.println(set);
            right++;
        }

        if (s.length() - left > maxLength) {
            maxLength = s.length() - left;
        }


        return maxLength;
    }
}
