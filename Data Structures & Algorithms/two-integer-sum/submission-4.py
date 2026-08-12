class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        prev = {}
        for i in range(n):
            num = nums[i]
            if target - num in prev:
                return [prev[target-num], i]
            prev[num] = i
        
        return [-1, -1]