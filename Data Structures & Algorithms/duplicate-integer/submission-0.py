class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hist = {}
        duplicata = False
        for n in nums:
            if n in hist:
                duplicata = True
                return duplicata
            else:
                hist[n] = 1
        
        return duplicata
