class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            for c in word:
                s += str(ord(c)) + " "
            s += "999 "
        return s
    
    def decode(self, s: str) -> List[str]:
        res = []
        nums = s.split()
        word = ""
        for i in range(len(nums)):
            if nums[i] == "999":
                res.append(word)
                word = ""
            else:
                word += chr(int(nums[i]))
        return res