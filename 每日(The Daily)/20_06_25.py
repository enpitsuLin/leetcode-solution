class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        len_s = (len(s) + 1)
        dp = [False] * len_s
        dp[0] = True
        for i in range(1, len_s):
            for j in range(i):
                if(dp[j] & (s[j:i] in wordDict)):
                    dp[i] = True
                    break
        return dp[-1]
if __name__ == "__main__":
    app = Solution()
    print(app.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))