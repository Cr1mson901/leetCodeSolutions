class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows >= len(s):
            return s
        output = ""
        groupSize = numRows - 1
        numGroups = -(len(s)//-(groupSize))
        groups = []
        for i in range(numGroups-1):
            groups.append(s[i*groupSize:(i+1)*groupSize])
        groups.append(s[(numGroups-1)*groupSize:])
        for i in range(numRows):
            if i == 0:
                for j in range(0,numGroups,2):
                    output += groups[j][i]
                continue
            if i == (numRows-1):
                for j in range(1,numGroups,2):
                    output += groups[j][0]
                continue
            for j in range(0,numGroups):
                try:
                    if j % 2 == 0:
                        output += groups[j][i]
                    else:
                        output += groups[j][groupSize-i]
                except:
                    continue
        return output
# A much smarter solution not courtesy of mwa
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        idx, change = 0,1
        for char in s:
            rows[idx] += char
            if idx == 0:
                change = 1
            if idx == numRows-1:
                change = -1
            idx += change
        return "".join(rows)