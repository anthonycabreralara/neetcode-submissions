class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = Counter(nums)
        freq = [[] for _ in range(n+1)]
        
        for key in count:
            freq[count[key]].append(key)
        
        res = []
        for i in range(n, -1, -1):
            while k > 0 and freq[i]:
                curr = freq[i].pop()
                k -= 1
                res.append(curr)

        return res
