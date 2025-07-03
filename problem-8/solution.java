class Solution {
    public int myAtoi(String s) {
        int sign = 1;
        int result = 0;
        int i = 0;

        while (i < s.length()) {
            char c = s.charAt(i);
            if (!isWhitespace(c)) {
                break;
            }

            i++;
        }

        if (i < s.length() && isSign(s.charAt(i))) {
            sign = getSign(s.charAt(i));
            i++;
        }

        while (i < s.length()) {
            char c = s.charAt(i);
            if (!isDigit(c)) {
                break;
            }
            
            int newDigit = getDigit(c);
            if (doesOverflow(result, sign, newDigit)) {
                result = sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
                break;
            }

            result = (result * 10) + (sign * getDigit(c));

            i++;
        }

        return result;
    }

    private boolean isWhitespace(char c) {
        return c == ' ';
    }

    private boolean isSign(char c) {
        return c == '-' || c == '+';
    }

    private int getSign(char c) {
        if (c == '-') {
            return -1;
        }

        return 1;
    }

    private boolean isDigit(char c) {
        return (int) c >= (int) '0' && (int) c <= (int) '9';
    }

    private int getDigit(char c) {
        return (int) c - (int) '0';
    }

    private boolean doesOverflow(int currentResult, int sign, int newDigit) {
        if (sign == 1) {
            return (Integer.MAX_VALUE - newDigit) / 10 < currentResult;
        } else {
            return (Integer.MIN_VALUE + newDigit) / 10 > currentResult;
        }
    }
}