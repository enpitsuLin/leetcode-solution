import math

# 方法：暴力


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        res = 0
        for i in range(n):
            nums.append(2 * i + start)
        for i in nums:
            if res == 0:
                res = i
            else:
                res = res ^ i
        return res

# 方法二：O(1) 位运算


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            if i == 0:
                res = math.floor(start/2)
            else:
                res = res ^ math.floor((2 * i + start)/2)

        if(start % 2 == 0 or n % 2 == 0):
            res = 2*res
        else:
            res = 2*res + 1
        return res


if __name__ == "__main__":
    s = Solution()
    s.xorOperation(n=4, start=3)
