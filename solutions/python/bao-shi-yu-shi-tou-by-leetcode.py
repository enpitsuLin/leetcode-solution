#方法一：暴力
class Solution(object):
    def numJewelsInStones(self, J, S):
        return sum(s in J for s in S)
#方法二：哈希
class Solution(object):
    def numJewelsInStones(self, J, S):
        Jset = set(J)
        return sum(s in Jset for s in S)
