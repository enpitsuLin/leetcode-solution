class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a and not b:return ''
        a_front = a[0:-1] 
        b_front = b[0:-1] 
        a_last = a[-1:]
        b_last = b[-1:]
        if a_last =='1' and b_last == '1':
            tmp = self.addBinary("1",b_front)
            res =  self.addBinary(a_front,tmp) + '0'
            return res
        elif a_last == '1' or b_last == '1':
            res = self.addBinary(a_front,b_front) + '1'
            return res
        else:
            res = self.addBinary(a_front,b_front) +  '0'
            return res

if __name__ == "__main__":
    app = Solution()
    print(app.addBinary(a = "11", b = "111"))