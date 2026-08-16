class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in nums:
                curr = num
                while curr in nums:
                    curr += 1
                res = max(res, curr - num)
        return res