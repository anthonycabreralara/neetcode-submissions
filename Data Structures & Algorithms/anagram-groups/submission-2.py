class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        # a = 97
        for s in strs:
            curr = [0 for _ in range(26)]
            for c in s:
                curr[ord(c) - 97] += 1
            curr = tuple(curr)
            
            if curr in groups:
                groups[curr].append(s)
            else:
                groups[curr] = [s]

        res = []
        for k in groups:
            res.append(groups[k])
        
        return res