class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_product = [1] * len(nums)
        left_product = [1] * len(nums)

        product = 1
        for i in range(len(nums)):
            left_product[i] = product
            product  = product * nums[i]

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            right_product[i] = product
            product = product * nums[i]

        for i in range(len(nums)):
            nums[i] = right_product[i] * left_product[i]


        return nums