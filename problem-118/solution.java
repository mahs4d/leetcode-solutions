class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new LinkedList<>();
        if (numRows == 0) {
            return result;
        }

        result.add(new LinkedList<Integer>(Arrays.asList(1)));
        for (int i = 0; i < numRows - 1; i++) {
            List<Integer> row = new LinkedList<>();
            int previousValue = 0;
            for (int value : result.getLast()) {
                row.add(value + previousValue);
                previousValue = value;
            }
            row.add(1);
            result.add(row);
        }
        return result;
    }
}
