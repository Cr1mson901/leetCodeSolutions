class Solution:
    def reverseWords(self, s: str) -> str:
        my_lst = s.split(" ")
        my_lst = [word for word in my_lst if len(word) > 0]
        if len(my_lst) == 1:
            return my_lst[0]
        my_lst.reverse()
        result = ""
        for i in range(len(my_lst)-1):
            result += my_lst[i] + " "
        result += my_lst[-1]
        return result