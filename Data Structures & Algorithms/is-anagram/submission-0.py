class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_character_count = {}
        t_character_count = {}

        for character in s:
            if (character in s_character_count):
                s_character_count[character] = s_character_count[character] + 1
            else:
                s_character_count[character] = 1
        
        for character in t:
            if (character in t_character_count):
                t_character_count[character] = t_character_count[character] + 1
            else:
                t_character_count[character] = 1
        
        if s_character_count != t_character_count:
            return False

        return True
            
        