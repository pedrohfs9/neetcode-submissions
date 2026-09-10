class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        indo = ''
        voltando = ''

        for char in range(0, len(s)):
            if s[left].isalnum():
                indo += s[left]
            
            if s[right].isalnum():
                voltando += s[right]
            
            left += 1
            right -= 1
        
        if indo.lower() == voltando.lower():
            return True
        else:
            return False
