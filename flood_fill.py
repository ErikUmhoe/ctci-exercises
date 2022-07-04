from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        numRows = len(image)
        numCols = len(image[0])
        if image[sr][sc] == color:
            return
        self._floodFill(image, sr, sc, color, numRows, numCols, image[sr][sc])
        return image

    def _floodFill(self, image, sr, sc, color, numRows, numCols, valToColor):
        if sr < 0 or sr >= numRows:
            return
        if sc < 0 or sc >= numCols:
            return image
        image[sr][sc] = color
        if (sr-1) >= 0 and image[sr-1][sc] == valToColor:
            image[sr-1][sc] = color
            self._floodFill(image, sr-1, sc, color, numRows, numCols, valToColor)
        if (sr+1) < numRows and image[sr+1][sc] == valToColor:
            image[sr+1][sc] = color
            self._floodFill(image, sr+1, sc, color, numRows, numCols, valToColor)
        if (sc-1) >= 0 and image[sr][sc-1] == valToColor:
            image[sr][sc-1] = color
            self._floodFill(image, sr, sc-1, color, numRows, numCols, valToColor)
        if (sc+1) < numCols and image[sr][sc+1] == valToColor:
            image[sr][sc+1] = color
            self._floodFill(image, sr, sc+1, color, numRows, numCols, valToColor)
        return
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
sol = Solution()
print(sol.floodFill(image, sr,sc,color))
