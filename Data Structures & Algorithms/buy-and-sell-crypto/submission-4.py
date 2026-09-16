class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maximo = 0

        while (right < len(prices)):
  
            maximo = max(maximo, prices[right] - prices[left])
            
            if prices[left] > prices[right]:
                right += 1
                left = right - 1                 
            else:
                right += 1
        
        return maximo
