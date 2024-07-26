# Wtf even is this code. Doesn't work
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if newInterval[0] < intervals[0][0]:
            finding_start = False
            intervals[0][0] = newInterval[0]
        else:
            finding_start = True
        start = 0
        while finding_start:
            if newInterval[0] in range(intervals[start][0],intervals[start][1]+1):
                finding_start = False
            else:
                start += 1
        if newInterval[1] > intervals[-1][1]:
            intervals[start][1] = newInterval[1]
            combining = False
            intervals = intervals[:start+1]
        else:
            combining = True
            end = start
        while combining:
            if newInterval[1] in range(intervals[end][0],intervals[end][1]+1):
                intervals[start][1] = intervals[end][1]
                combining = False
            elif newInterval[1] < intervals[end][0]:
                intervals[start][1] = newInterval[1]
                break
            if end > start:
                intervals.pop(end)
            else:
                end += 1
        return intervals
    
