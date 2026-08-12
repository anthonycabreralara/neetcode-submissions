class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        history = set()
        for nums in nums:
            if nums in history:
                return True
            else:
                history.add(nums)

        return False