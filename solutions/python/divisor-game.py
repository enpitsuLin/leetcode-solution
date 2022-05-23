class Solution:
    def divisorGame(self, N: int) -> bool:
        target = [False for i in range(N + 1)]
        target[1] = False #若爱丽丝抽到1，则爱丽丝输
        if N <= 1:
            return False
        else:
            target[2] = True #若爱丽丝抽到2，则爱丽丝赢
            for i in range(3, N+1):
                for j in range(1, i//2):
                    # 若j是i的余数且target[i-j]为假（0）的话，则代表当前为真（1）
                    if i % j==0 and not target[i - j]:
                        target[i] = True
                        break
            return target[N]
