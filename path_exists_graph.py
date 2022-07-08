from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
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
        marked = {}
        self._dfs(source, destination, marked, ht)
        return destination in marked
    def _dfs(self, source, destination, marked, ht):
        if source not in marked:
            marked[source] = True
            for node in ht[source]:
                self._dfs(node, destination, marked, ht)
sol = Solution()
edges = [[0,1],[1,2],[2,0]]
n = 3
source = 0
destination = 2
print(sol.validPath(n, edges, source, destination))
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
print(sol.validPath(n, edges, source, destination))
edges = [[1,0],[3,1],[0,4],[2,1]]
source = 0
destination = 2
n = 5
print(sol.validPath(n, edges, source, destination))