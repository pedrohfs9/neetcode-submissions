class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_matrix = [item for linha in matrix for item in linha]

        left = 0
        right = len(flat_matrix) - 1

        while left <= right:
            meio = int(left + (right - left)/2)
            if flat_matrix[meio] == target:
                return True
            elif target > flat_matrix[meio]:
                left = meio + 1
            else:
                right = meio - 1
        
        return False
