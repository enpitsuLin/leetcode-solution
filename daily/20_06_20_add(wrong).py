class Solution:
    """ 动态规划 """
    def f(self, s:str, p:str, i:int, j:int, results:list) -> bool:
        if p[i] == '*':
            m_ij = p[i - 1] == s[j] or p[i - 1] == '.'
            result = (results[i - 2][j] | results[i - 1][j] | results[i][j - 1]) & m_ij
        else:
            m_ij = p[i] == s[j] or p[i] == '.'
            result = results[i - 1][j - 1] & m_ij
        return result

    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s) + 1
        len_p = len(p) + 1
        results = [[False] * len_s for i in range(len_p)] #建立二维数组做缓存
        results[0][0] = True
        p = '_' + p
        s = '_' + s
        #异常处理
        if len_p == len_s == 1:
            return True
        elif len_p == 1:
            return False
        elif p[0] == "*":
            return False

        for i in range(1, len_p):
            if p[i] =='*':
                results[i][0] = results[i - 2][0]
            for j in range(1, len_s):
                results[i][j] = self.f(s,p,i,j,results)
        return results[-1][-1]

if __name__ == "__main__":
    app = Solution()
    print(app.isMatch("aaa"
,"aaab*"))