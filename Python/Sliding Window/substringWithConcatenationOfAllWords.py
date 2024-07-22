class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        size = len(words[0])
        output = []
        correct = False
        for i in range(len(s)-(len(words)*size)+1):
            if s[i-1] == s[i+(size*len(words))-1] and size == 1 and correct == True:
                output.append(i)
                continue
            checklist = words[:]
            try:
                for j in range(len(words)):
                    word = s[i + (size * j):i + size + (size * j)]
                    if word in checklist:
                        checklist.remove(word)
                    else:
                        raise Exception("Nope")
            except:
                correct = False
                continue
            correct = True
            output.append(i)
        return output
