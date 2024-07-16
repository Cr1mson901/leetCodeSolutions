class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = list(strs[0])
        counter = 0
        for i in range(len(first_word)):
            try:
                for j in range(1, len(strs)):
                    if first_word[i] != strs[j][i]:
                        raise Exception("Not Matching")
                counter += 1
            except:
                break
        return(strs[0][:counter])