from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        basket1 = [None,0]
        basket2 = [None,0]
        size = 0
        for i in range(len(fruits)):
            if basket1[0] == fruits[i]:
                basket1[1] += 1
            elif basket2[0] == fruits[i]:
                basket2[1] += 1
            elif basket1[0] is None:
                basket1[0] = fruits[i]
                basket1[1] = 1
            elif basket2[0] is None:
                basket2[0] = fruits[i]
                basket2[1] = 1
            else:
                while True:
                    if basket1[0] == fruits[start]:
                        basket1[1] -= 1
                        start += 1
                        if basket1[1] == 0:
                            basket1[0] = fruits[i]
                            basket1[1] = 1
                            break
                    else:
                        basket2[1] -= 1
                        start += 1
                        if basket2[1] == 0:
                            basket2[0] = fruits[i]
                            basket2[1] = 1
                            break
            size = max(size, basket1[1] + basket2[1])
        return size
    
sol = Solution()
fruits = [0,1,2,2] 
print(sol.totalFruit(fruits)) # 3
fruits = [3,3,3,1,2,1,1,2,3,3,4]
print(sol.totalFruit(fruits)) # 5
fruits = [1,0,1,4,1,4,1,2,3]
print(sol.totalFruit(fruits)) # 5
fruits = [0,1,6,6,4,4,6]
print(sol.totalFruit(fruits)) # 5