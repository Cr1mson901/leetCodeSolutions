# Lambdas are sick
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 1
        intervals.sort(key=lambda x: x[0])
        while i < len(intervals):
            if intervals[i][0] in range(intervals[i-1][0],intervals[i-1][1] + 1):
                if intervals[i][1] > intervals[i-1][1]:
                    intervals[i-1][1] = intervals[i][1]
                intervals.pop(i)
            else:
                i += 1
        return intervals