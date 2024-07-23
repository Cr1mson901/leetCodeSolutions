# Too slow
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         if len(strs) < 2:
#             return [strs]
#         freq_maps = []
#         output = []
#         for word in strs:
#             try:
#                 freq_map = {}
#                 for letter in word:
#                     freq_map[letter] = freq_map.get(letter,0) + 1
#                 for idx, freq in enumerate(freq_maps):
#                     if freq == freq_map:
#                         output[idx].append(word)
#                         raise Exception("break")
#                 freq_maps.append(freq_map)
#                 output.append([word])
#             except:
#                 continue
#         return output
    
# Slightly faster but still pretty shit
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        sorted_map = []
        output = []
        for word in strs:
            try:
                sort_words = [letter for letter in word]
                sort_words.sort()
                for idx, sort in enumerate(sorted_map):
                    if sort == sort_words:
                        output[idx].append(word)
                        raise Exception("break")
                output.append([word])
                sorted_map.append(sort_words)
            except:
                continue
        return output
# A much smarter answer, need to look into defaultdict more
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            output[key].append(word)
        return output.values()
            
            
