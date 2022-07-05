import sys
from typing import List


class SlidingWindow:
    # Find max sum subarray of a fixed size K
    # E.g. [4,2,1,7,8,1,2,8,1,0], K = 3
    def findMaxSumArray(self, arr: List[int], k: int) -> int:
        maxValue = -sys.maxsize
        runningSum = 0
        # Grow initial window length
        for i in range(0, len(arr)):
            runningSum += arr[i]
            if i >= k-1:
                maxValue = max(maxValue, runningSum)
                runningSum -= arr[i-(k-1)]
        return maxValue

    # Find max sum subarray of a fixed size K
    # E.g. [4,2,1,7,8,1,2,8,1,0], sum >= 8
    def smallest_sub_array_for_sum(self, arr:List[int], sum: int) -> int:
        smallest = sys.maxsize
        runningSum = 0
        windowStart = 0
        for windowEnd in range(len(arr)):
            runningSum += arr[windowEnd]
            while(runningSum >= sum):
                smallest = min(smallest, windowEnd - windowStart + 1)            
                runningSum -= arr[windowStart]
                windowStart += 1
        return smallest

    def longest_substring_k_distinct_chars(self, substr: str, maxChars: int) -> str:
        longestStr = ""
        ht = {}
        currentStr = ""
        currDistinct = 0
        for ch in substr:
            currentStr += ch
            if ch not in ht:
                ht[ch] = 1
                currDistinct += 1
            else:
                ht[ch] += 1
            while currDistinct > maxChars:
                chToRemove = currentStr[0]
                while ht[chToRemove] > 0:
                    currentStr = currentStr[1:]   # Remove all instances of chToRemove from currenStr
                    ht[chToRemove] -= 1
                currDistinct -= 1
            longestStr = max(currentStr, longestStr, key=len)
        return longestStr
    
def main():
    arr = [4,2,1,7,8,1,2,8,1,0]
    k = 3
    sw = SlidingWindow()
    print(sw.findMaxSumArray(arr, k))
    print(sw.smallest_sub_array_for_sum(arr, 8))
    print(sw.longest_substring_k_distinct_chars("AAAHHIBC",2))
    
if __name__ == "__main__":
    main()
        