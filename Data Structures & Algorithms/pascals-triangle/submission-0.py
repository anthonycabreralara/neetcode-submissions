class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            curr = [1] * i
            if i > 2:
                for j in range(1,i-1):
                    curr[j] = res[-1][j] + res[-1][j-1]
            res.append(curr)
        return res