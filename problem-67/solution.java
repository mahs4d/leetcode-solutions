class Solution {
    public String addBinary(String a, String b) {
        int maxLength = Math.max(a.length(), b.length());

        char[] result = new char[maxLength + 1];
        char excess = '0';

        for (int i = 0; i < maxLength; i++) {
            char v1 = a.length() - i > 0 ? a.charAt(a.length() - i - 1) : '0';
            char v2 = b.length() - i > 0 ? b.charAt(b.length() - i - 1) : '0';

            int nOnes = excess == '1' ? 1 : 0;
            nOnes += v1 == '1' ? 1 : 0;
            nOnes += v2 == '1' ? 1 : 0;

            result[maxLength - i] = nOnes % 2 == 0 ? '0' : '1';
            excess = nOnes > 1 ? '1' : '0';
        }
        
        if (excess == '1') {
            result[0] = '1';
            return new String(result);
        } else {
            return new String(result).substring(1);
        }
    }
}