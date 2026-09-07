class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            histS = {}
            histT = {}
            for c in range(0, len(s)):
                if s[c] in histS:
                    histS[s[c]] += 1
                else:
                    histS[s[c]] = 1
                
                if t[c] in histT:
                    histT[t[c]] += 1
                else:
                    histT[t[c]] = 1
        
        if histS == histT:
            return True
        else:
            return False
