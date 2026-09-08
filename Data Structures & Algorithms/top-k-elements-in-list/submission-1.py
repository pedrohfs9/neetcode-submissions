class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencia = {}

        for n in range(0, len(nums)):
            if nums[n] in frequencia:
                frequencia[nums[n]] += 1
            else:
                frequencia[nums[n]] = 1
        
        ordenadas = sorted(frequencia, key=frequencia.get, reverse=True)
        ranking = {chave:frequencia[chave] for chave in ordenadas}
        top = list(ranking.keys())[:k]

        return top
        