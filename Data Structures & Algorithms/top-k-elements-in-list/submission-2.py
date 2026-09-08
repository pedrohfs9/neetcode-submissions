class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencia = {}

        for n in range(0, len(nums)):
            if nums[n] in frequencia:
                frequencia[nums[n]] += 1
            else:
                frequencia[nums[n]] = 1
        
        ordenado = sorted(frequencia, key=frequencia.get, reverse=True)
        return ordenado[0:k]
