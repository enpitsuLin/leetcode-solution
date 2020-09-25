class Solution:
    def matchPattern(self, pattern:str, value:str, length_a:int, length_b:int) -> bool:
        print("La:%s Lb:%s"%(length_a, length_b))
        str_a = ""
        str_b = ""
        pos = 0
        res = ""
        for p_now in pattern:
            if p_now == 'a':
                if str_a == "":
                    str_a = value[pos:pos + length_a]
                res += str_a
                pos += length_a
            elif p_now == 'b':
                if str_b == "":
                    str_b = value[pos:pos + length_b]
                res += str_b
                pos += length_b
        print("Sa:%s Sb:%s"%(str_a, str_b))
        #res = pattern.replace('b',str_b).replace('a',str_a)
        print(res)
        print(value)
        
        if res == value:
            return True
        return False
        
    
    def patternMatching(self, pattern: str, value: str) -> bool:
        if not len(value):
            return (pattern=="a")|(pattern=="b")|(pattern=="")
        if not len(pattern):
            return False
        count_a = 0
        count_b = 0
        res = False
        for i in pattern:
            if i=="a":
                count_a += 1
            else:
                count_b += 1
        print("Ca:%s Cb:%s"%(count_a,count_b))
        length_a_max = int(len(value)/count_a) if count_a != 0 else 0
        print(length_a_max)
        if length_a_max == 0:
            length_b = int(len(value)/len(pattern))
            res = self.matchPattern(pattern, value, 0, length_b)
        elif length_a_max == len(value):
            res = self.matchPattern(pattern, value, length_a_max, 0)
        else:
            for length_a in range(length_a_max+1):#枚举 i:La length_b:Lb
                length_b = int((len(value) - length_a * count_a)/(len(pattern)-count_a)) if len(pattern)-count_a != 0 else 0
                print("La:%s Lb:%s"%(length_a,length_b))
                if(length_a * count_a + length_b * count_b !=len(value)):continue
                if self.matchPattern(pattern, value, length_a, length_b):
                    res = True
                    break
            
        return res
                

if __name__ == "__main__":
    s = Solution()
    print(s.patternMatching("aaaaaa"
,"nnnnnn"))
    print('------')
    print(s.patternMatching("a"
,"zqvamqvuuvvazv"))
