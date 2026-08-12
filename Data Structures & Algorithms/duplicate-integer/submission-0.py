class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = []
        for num in nums:
            if (num in num_count):
                return True
            else:
                num_count.append(num)
        return False