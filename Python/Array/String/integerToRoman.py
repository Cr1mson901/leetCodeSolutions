class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        numerals = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        while num != 0:
            if str(num)[0] != "4" and str(num)[0] != "9":
                for key in numerals.keys():
                    if key <= num:
                        sub = key
                    else:
                        break
                num -= sub
                roman = roman + numerals[sub]
            else:
                for key in numerals.keys():
                    if key > num:
                        sub = key
                        break
                if str(num)[0] == "4":
                    tract = sub/5
                else:
                    tract = sub/10
                roman += numerals[tract]
                roman += numerals[sub]
                if num > 10:
                    num = int(str(num)[1:])
                else:
                    num = 0
        return roman
