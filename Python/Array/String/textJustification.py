#Fast code that was a pain in the ass to set up
class Solution:
    def fullJustify(self, words, maxWidth):
        lines = [[]]
        letters = 0
        row = 0
        output = []
        for word in words:
            if letters + len(word) <= maxWidth:
                lines[row].append(word)
                lines[row].append(1)
                letters += len(word) + 1
            else:
                # Removes the ending space
                if len(lines[row]) != 2 or len(lines[row][0]) == maxWidth: 
                    letters -= 1
                    lines[row].pop()
                idx = 1
                while letters < maxWidth:
                    if idx >= len(lines[row]):
                        idx = 1
                    letters += 1
                    lines[row][idx] += 1
                    idx += 2
                lines.append([word])
                letters = len(word) + 1
                row += 1
                lines[row].append(1)
        lines[row][-1] = maxWidth - letters + 1
        for i in range(row+1):
            output.append("")
            for j in range(len(lines[i])):
                if j % 2 == 1:
                    output[i] += " " * lines[i][j]
                else:
                    output[i] += lines[i][j]
        return output

