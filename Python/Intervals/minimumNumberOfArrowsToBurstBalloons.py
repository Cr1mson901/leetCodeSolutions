# Code I like but is not correct
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        targets = [points[0]]
        for balloon in points:
            try:
                hit = False
                for target in targets:
                    if balloon[0] in range(target[0],target[1]+1):
                        target[0] = balloon[0]
                        hit = True
                    if balloon[1] in range(target[0],target[1]+1):
                        target[1] = balloon[1]
                        hit = True
                    if hit:
                        raise Exception("Hit")
                targets.append(balloon)
            except:
                pass
        return len(targets)
            