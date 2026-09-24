class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters1 = {}
        letters2 = {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in letters1:
                    letters1[s[i]] += 1
                else:
                    letters1[s[i]] = 1
            for i in range(len(t)):
                if t[i] in letters2:
                    letters2[t[i]] += 1
                else:
                    letters2[t[i]] = 1
            if letters1 == letters2:
                return True
            else:
                return False
        else:
            return False
        
        
