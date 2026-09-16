class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        maximo = 1
        hist = {}

        if s == "":
            return 0
        
        hist[s[0]] = 1

        while right < len(s) - 1:
            right += 1

            if s[right] in hist:
                hist[s[right]] += 1
            else:
                hist[s[right]] = 1  
            
            while hist[s[right]] == 2:
                hist[s[left]] -= 1
                left += 1
            
            maximo = max(maximo, right-left+1)

        return maximo
