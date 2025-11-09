import math

MAX_VALUE = (2 ** 31) - 1
MIN_VALUE = -(2 ** 31)


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        x_length = self.get_x_length(x)
        for i in range(x_length):
            try:
                next_digit = x % 10 if x >= 0 else (x % 10) - 10
                next_digit = next_digit if next_digit != -10 else 0
                x = math.floor(x / 10) if x >= 0 else math.ceil(x / 10)
                reverse_digit_value = self.pow_10(next_digit, x_length - i - 1)
                result = self.add(result, reverse_digit_value)
            except:
                return 0
        return result


    def get_x_length(self, x: int) -> int:
        n = x
        i = 0
        while n != 0:
            n = math.floor(n / 10) if n >= 0 else math.ceil(n / 10)
            i += 1
        return i

    def pow_10(self, a: int, b: int) -> int:
        result = a
        for i in range(b):
            if result >= 0 and result > (MAX_VALUE / 10):
                raise Exception(f"Invalid pow {a} ** {b}")

            if result < 0 and result < (MIN_VALUE / 10):
                raise Exception(f"Invalid pow {a} ** {b}")

            result = result * 10

        return result

    def add(self, a: int, b: int) -> int:
        if a >= 0 and a > MAX_VALUE - b:
            raise Exception(f"Invalid add {a} + {b}")

        if a < 0 and a < MIN_VALUE - b:
            raise Exception(f"Invalid add {a} + {b}")

        return a + b