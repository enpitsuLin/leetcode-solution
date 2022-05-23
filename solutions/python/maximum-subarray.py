class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + dp[i - 1] if dp[i - 1]>0 else nums[i]
        max = 0
        for i in dp:
            if i > max:
                max = i
        return max

if __name__ == "__main__":
    app = Solution()
    print(app.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))