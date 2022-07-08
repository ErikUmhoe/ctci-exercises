from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        ht = {}
        for e in edges:
            if e[0] not in ht:
                ht[e[0]] = [e[1]]
            else:
                ht[e[0]].append(e[1])
            if e[1] not in ht:
                ht[e[1]] = [e[0]]
            else:
                ht[e[1]].append(e[0])
        pairs = 0
        for i in range(n):
            for j in range(i+1, n):
                    marked = {}
                    self._dfs(i, j, marked, ht)
                    if j not in marked:
                        pairs += 1
        return pairs
    
    def _dfs(self, nodeA, nodeB, marked, ht):
        if nodeA not in marked and nodeA in ht:
            marked[nodeA] = True
            for node in ht[nodeA]:
                self._dfs(node, nodeB, marked, ht)
    
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
sol = Solution()
print(sol.countPairs(7, edges))
edges = [[0,1],[0,2],[1,2]]
print(sol.countPairs(3, edges))
edges = [[1,0],[3,1],[0,4],[2,1]]
print(sol.countPairs(5, edges))
                    