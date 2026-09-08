class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        else:
            dicionario = {}
            for palavra in strs:
                ordenado = "".join(sorted(palavra))

                if ordenado in dicionario:
                    dicionario[ordenado].append(palavra)
                else:
                    dicionario[ordenado] = [palavra]
            
            return list(dicionario.values())