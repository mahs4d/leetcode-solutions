class Solution {
    public int climbStairs(int n) {
        if (n <= 1) {
            return n;
        }

        int p1 = 0;
        int p2 = 1;
        for (int i = n - 1; i >= 0; i--) {
            int tmp = p2 + p1;
            p1 = p2;
            p2 = tmp;
        }

        return p2;
    }
}