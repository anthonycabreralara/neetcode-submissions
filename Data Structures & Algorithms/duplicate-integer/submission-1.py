class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        history = []
        for item in nums:
            if item in history:
                return True
            else:
                history.append(item)

        return False
         