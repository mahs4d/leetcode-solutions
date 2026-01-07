class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<Integer>(1);
        row.add(1);

        for (int i = 0; i < rowIndex; i++) {
            row = generateNextRow(row);
        }
        return row;
    }

    private List<Integer> generateNextRow(List<Integer> previousRow) {
        List<Integer> result = new ArrayList<Integer>(previousRow.size() + 2);

        int prevValue = 0;
        for (int value : previousRow) {
            result.add(prevValue + value);
            prevValue = value;
        }

        result.add(1);
        return result;
    }
}
