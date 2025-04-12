class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose=[]
        for i in range(len(matrix[0])):
            element = []
            for j in range(len(matrix)):
                element.append(matrix[j][i])
            transpose.append(element)
        return transpose
