class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k: return []
        if k == 1: return [[i] for i in range(1, n+1)]
        res = []
        def helper(up, depth):
            if depth == k: res.append(up); return
            for i in range(up[-1]+1, n+2+depth-k): helper(up+[i], depth+1)
        for i in range(1, n+2-k): helper([i], 1)
        return res

if __name__ == "__main__":
    app = Solution()
    print(app.combine(n = 4, k = 2))