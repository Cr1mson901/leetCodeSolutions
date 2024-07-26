#The code still looks gross but it does work and is fast
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i, newInterval)
                break
            elif newInterval[0] in range(intervals[i][0], intervals[i][1]+1):
                break
        start = i
        for j in range(len(intervals)-1,start-1,-1):
            if newInterval[1] > intervals[j][1]:
                intervals[start][1] = newInterval[1]
                try:
                    del intervals[start+1:j+1]
                except:
                    pass
                break
            elif newInterval[1] in range(intervals[j][0],intervals[j][1]+1):
                intervals[start][1] = intervals[j][1]
                try:
                    del intervals[start+1:j+1]
                except:
                    pass
                break
        return intervals
    
