class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""
        size = float('inf')
        missing = {}
        window = []
        for i in range(len(t)):
            if t[i] in missing:
                missing[t[i]] += 1
            else:
                missing[t[i]] = 1      
        if len(t) > len(s):
            return output
        for i in range(len(s)):
            window.append(s[i])
            if s[i] in t:
                missing[s[i]] -= 1
                while window[0] not in t:
                    del window[0]
                while missing[window[0]] < 0:
                    missing[window[0]] += 1
                    del window[0]
                    while window[0] not in t:
                        del window[0]
                if all(0 >= value for value in missing.values()) and size > len(window):
                    output = window[:]
                    size = len(window)
        return "".join(output)

