from typing import Dict
import time

def num_ways_dp(numStairsLeft: int):
    ways = [0] * numStairsLeft
    return _num_ways(numStairsLeft - 1, ways) + _num_ways(numStairsLeft - 2, ways) + _num_ways(numStairsLeft - 3, ways)

def _num_ways(numStairsLeft: int, stairsClimbed):
    if numStairsLeft == 1:
        return 1
    if numStairsLeft == 2:
        return 2
    if numStairsLeft == 3:
        return 4
    if numStairsLeft not in stairsClimbed:
        stairsClimbed[numStairsLeft] = _num_ways(numStairsLeft - 1, stairsClimbed) + _num_ways(numStairsLeft - 2, stairsClimbed) + _num_ways(numStairsLeft - 3, stairsClimbed)
    return stairsClimbed[numStairsLeft]
    
def num_ways(numStairsLeft: int):
    if numStairsLeft == 1:
        return 1
    if numStairsLeft == 2:
        return 2
    if numStairsLeft == 3:
        return 4
    return num_ways(numStairsLeft - 1) + num_ways(numStairsLeft - 2) + num_ways(numStairsLeft - 3)

n = 30
start = time.perf_counter()
nw = num_ways(n)
stop = time.perf_counter()
print(f"{nw}: {stop - start} seconds.")
start = time.perf_counter()
nw = num_ways_dp(n)
stop = time.perf_counter()
print(f"{nw}: {stop - start} seconds")
