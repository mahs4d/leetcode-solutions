class Solution {
    public boolean isPalindrome(int x) {
        String intString = String.valueOf(x);

        int i = 0;
        int j = intString.length() - 1;
        while (i < j) {
            if (intString.charAt(i) != intString.charAt(j)) {
                return false;
            }

            i += 1;
            j -= 1;
        }

        return true;
    }
}