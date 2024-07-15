class Solution:
    def candy(self, ratings: List[int]) -> int:
        total = [1 for x in range(len(ratings))]
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                total[i] = total[i-1] + 1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1] and total[i] <= total[i+1]:
                total[i] = total[i+1] + 1
        return sum(total)