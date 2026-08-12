class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sDict = {}
        for s in strs:
            l = [0, ] * 26
            for c in s:
                l[ord(c) - 97] += 1
            t = tuple(l)
            if t in sDict:
                sDict[t].append(s)
            else:
                sDict[t] = [s]
        
        res = []
        for k in sDict:
            res.append(sDict[k])
        
        return res
        