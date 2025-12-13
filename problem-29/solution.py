class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_value = 2 ** 31 - 1
        min_value = -2 ** 31

        sign = 1 if (dividend >= 0) == (divisor >= 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        r = 0
        for i in range(31, -1, -1):
            new_digit = (dividend & (1 << i)) >> i
            x = (r << 1) + new_digit

            if x >= divisor:
                result = (result << 1) + 1
                r = x - divisor
            else:
                result = result << 1
                r = x
        
        result = result * sign
        result = min(result, max_value)
        result = max(result, min_value)

        return result
