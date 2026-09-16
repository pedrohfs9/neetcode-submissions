class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maximo = 0

        while (right < len(prices)) and (left < len(prices)):

            if right > left:
                maximo = max(maximo, prices[right] - prices[left])
            else:
                maximo = max(maximo, prices[left] - prices[right])
            
            if prices[left] > prices[right]:
                if right == 1:
                    left += 1
                    right += 1
                else:
                    right += 1
                    left = right - 1                 
            else:
                right += 1
        
        return maximo
