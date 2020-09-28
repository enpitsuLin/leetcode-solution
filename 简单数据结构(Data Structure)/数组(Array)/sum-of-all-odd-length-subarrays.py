# 方法一 暴力枚举
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(0, len(arr)):
            sz = 1
            while(sz + i - 1 < len(arr)):
                res += sum(arr[i:i+sz])
                sz += 2
        return res


# O(n) 还没弄懂 见：https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/solution/cong-on3-dao-on-de-jie-fa-by-liuyubobobo/
