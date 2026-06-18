class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -(1 << 31)
        INT_MAX = (1 << 31) - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)

        dvd = abs(dividend)
        dvs = abs(divisor)

        quotient = 0

        for i in range(31, -1, -1):
            if (dvs << i) <= dvd:
                dvd -= dvs << i
                quotient |= 1 << i

        return -quotient if negative else quotient  