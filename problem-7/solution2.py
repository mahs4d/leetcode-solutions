import math

MAX_VALUE = (2 ** 31) - 1
MIN_VALUE = -(2 ** 31)


class Solution:
    def reverse(self, x: int) -> int:
        return self.reverse_helper(x, 0)

    def reverse_helper(self, x: int, reversed: int) -> int:
        if x == 0:
            return reversed

        if reversed > MAX_VALUE / 10 or reversed < MIN_VALUE / 10:
            return 0

        next_digit = (x % 10) if x >= 0 else (x % 10) - 10
        next_digit = next_digit if next_digit != -10 else 0

        reversed = reversed * 10 + next_digit
        x = math.floor(x / 10) if x >= 0 else math.ceil(x / 10)

        return self.reverse_helper(x, reversed)
