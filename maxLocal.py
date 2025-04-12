class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result=[]
        elementNum = len(grid)-2

        for i in range(elementNum):
            element = []
            for j in range (elementNum):
                ele = max(grid[x][y] for x in range(i, i+3) for y in range(j, j+3))
                element.append(ele)
            result.append(element)
        return result
