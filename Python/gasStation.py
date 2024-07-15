# Too Slow
# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         if sum(cost) > sum(gas):
#             return -1
#         if len(gas) == 1: return 0
#         road_map = []
#         output = {}
#         for i in range(len(gas)):
#             dif = gas[i] - cost[i]
#             road_map.append(dif)
#             if dif > 0:
#                 output[i] = dif
#         counter = 1
#         while len(output) > 1:
#             for station in output.keys():
#                 output[station] += road_map[station - len(gas) + counter]
#             temp = list(output.keys())
#             for key in temp:
#                 if output[key] < 0:
#                     del output[key]
#             counter += 1
#         return list(output.keys())[0]

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        total = 0
        station = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                station = i + 1
        return station


            
