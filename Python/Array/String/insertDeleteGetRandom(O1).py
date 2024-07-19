class RandomizedSet:

    def __init__(self):
        self.numList = []
        self.numMap = {}

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        else:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.numMap:
            index = self.numMap[val]
            lst_val = self.numList[-1]
            self.numList[index] = lst_val
            self.numList.pop()
            self.numMap[lst_val] = index
            del self.numMap[val]
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()