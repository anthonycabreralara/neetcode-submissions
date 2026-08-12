class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nums = set(nums)

        return len(nums) < n