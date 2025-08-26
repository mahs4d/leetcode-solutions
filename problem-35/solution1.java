class Solution {
    public int searchInsert(int[] nums, int target) {
        int upperBoundIndex = nums.length;
        int lowerBoundIndex = -1;

        while (upperBoundIndex > lowerBoundIndex + 1) {
            int middleIndex = (upperBoundIndex + lowerBoundIndex) / 2;
            int value = nums[middleIndex];

            if (value < target) {
                lowerBoundIndex = middleIndex;
            } else if (value > target) {
                upperBoundIndex = middleIndex;
            } else {
                return middleIndex;
            }
        }
        return upperBoundIndex;
    }
}