class Solution:
    def isHappy(self, n: int) -> bool:
        stop = [n]
        n = list(map(int,str(n)))
        running = True
        while running:
            n = list(map(lambda x: x * x,n))
            n = sum(n)
            if n == 1:
                running = False
            elif n in stop:
                return False
            stop.append(n)
            n = list(map(int,str(n)))
        return True
