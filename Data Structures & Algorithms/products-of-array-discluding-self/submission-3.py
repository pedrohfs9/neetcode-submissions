from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tamanho = len(nums)
        prenum = [1] * tamanho
        posnum = [1] * tamanho
        output = [1] * tamanho

        for n in range(1, tamanho):
            prenum[n] = nums[n-1] * prenum[n-1]

        for i in range(tamanho-2, -1, -1):
            posnum[i] = nums[i+1] * posnum[i+1]
        
        for j in range(0, tamanho):
            output[j] = prenum[j] * posnum[j]
        
        return output
