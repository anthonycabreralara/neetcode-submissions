from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # Create buckets where index is frequency and value is list of numbers with that frequency
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        # Gather the top k frequent elements from the bucket (starting from the highest frequency)
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
