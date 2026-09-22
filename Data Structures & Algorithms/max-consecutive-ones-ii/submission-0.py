class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        k = 1
        res = 0
        n = len(nums)
        for r in range(n):
            if nums[r] == 0:
                k -= 1
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            res = max(res, r - l + 1)
        return res
