class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        res = 0
        curr = 0
        for i in range(n):
            left[i] = curr
            curr = max(curr, height[i])
        
        curr = 0
        for i in range(n-1, -1, -1):
            right[i] = curr
            curr = max(curr, height[i])

        for i in range(n):
            curr = min(left[i], right[i])
            curr -= height[i]
            if curr > 0:
                res += curr

        return res