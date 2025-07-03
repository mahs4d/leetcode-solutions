class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int originalValue = x;
        int reverseValue = 0;
        while (x > 0) {
            int rightDigit = x % 10;
            reverseValue = (reverseValue * 10) + rightDigit;
            x /= 10;
        }

        return reverseValue == originalValue;
    }
}