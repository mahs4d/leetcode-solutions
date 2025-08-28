class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        result = []
        diff = 2 * (numRows - 1)
        for row_n in range(numRows):
            i = 0
            j = 0
            k = 1
            is_mid_point = False
            prev_value = None
            while True:
                if not is_mid_point:
                    value = row_n + (j * diff)
                    j += 1
                else:
                    value = (k * diff) - row_n
                    k += 1

                if value >= len(s):
                    break

                if value != prev_value:
                    result.append(value)
                    prev_value = value

                i += 1
                is_mid_point = not is_mid_point

        return ''.join(s[i] for i in result)
