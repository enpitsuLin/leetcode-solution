class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add, mul = 0, 1
        while n > 0:
            digit = n % 10
            n //= 10
            add += digit
            mul *= digit
        return mul - add