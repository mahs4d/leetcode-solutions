import java.util.Stack;

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        Stack<Integer> stack = new Stack<>();

        int value = x;
        while (value > 0){
            int rightDigit = value % 10;
            stack.push(rightDigit);
            value /= 10;
        }

        while (x > 0) {
            int rightDigit = x % 10;
            int stackTop = stack.pop();
            if (stackTop != rightDigit) {
                return false;
            }
            x /= 10;
        }

        return stack.empty();
    }
}