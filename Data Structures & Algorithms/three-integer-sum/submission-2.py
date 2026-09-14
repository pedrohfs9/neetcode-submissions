class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ordenado = sorted(nums)
        aceitos = []

        for n in range(0, len(ordenado)):
            left = n+1
            right = len(ordenado) - 1
            if ordenado[n] == ordenado[n-1] and n > 0:
                continue  
            while left < right:
                
                atual = ordenado[n]

                soma = atual + ordenado[left] + ordenado[right]

                if soma == 0:
                    aceitos.append([atual, ordenado[left], ordenado[right]])
                    left += 1
                    while left < right and ordenado[left] == ordenado[left-1]:
                        left += 1
                elif soma > 0:
                    right -= 1
                else:
                    left += 1

        return aceitos
