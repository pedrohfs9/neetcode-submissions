class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)

        indo = ''
        voltando = ''

        for char in range(0, len(s)):
            if s[char].isalnum():
                indo += s[char]
        
        for char in range(len(s)-1, -1, -1):
            if s[char].isalnum():
                voltando += s[char]
        
        if indo.lower() == voltando.lower():
            return True
        else:
            return False
