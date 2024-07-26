#Edited the code to pass the 10,000 case but it still isn't good
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        targets = [points[0]]
        for balloon in points:
            try:
                hit = False
                if balloon[0] > targets[-1][1]:
                    targets.append(balloon)
                    raise Exception("too far")
                elif balloon[1] < targets[0][0]:
                    targets.insert(0,balloon)
                    raise Exception("too close")
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

#Similar idea just much smarter, also range is slow. Use greater then and less thens
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        count = 0
        arrow = float('-inf')
        for balloon in points:
            if balloon[1] >= arrow >= balloon[0]:
                continue
            else:
                count += 1
                arrow = balloon[1]
        return count