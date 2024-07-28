class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = int(a) + int(b)
        output = [int(x) for x in str(output)]
        for i in range(len(output)-1,0,-1):
            if output[i] > 1:
                output[i] -= 2
                output[i-1] += 1
        if output[0] > 1:
            output[0] -= 2
            output.insert(0,1)
        return "".join(map(str,output))
