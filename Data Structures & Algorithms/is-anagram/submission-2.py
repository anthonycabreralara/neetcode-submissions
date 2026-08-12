class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sTracker = {}
        tTracker = {}
        for i in range(len(s)):
            sTracker[s[i]] = sTracker.get(s[i], 0) + 1
            tTracker[t[i]] = tTracker.get(t[i], 0) + 1

        if len(sTracker) != len(tTracker):
            return False
        
        for k in sTracker:
            if sTracker.get(k) != tTracker.get(k):
                return False

        return True