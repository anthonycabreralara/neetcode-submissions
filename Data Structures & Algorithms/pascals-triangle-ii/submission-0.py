class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        tri = [[1], [1, 1]]
        for i in range(2, rowIndex+1):
            newRow = [1] * (i + 1)
            for j in range(1, len(newRow)-1):
                newRow[j] = tri[-1][j] + tri[-1][j-1]
            tri.append(newRow)
        
        return tri[-1]