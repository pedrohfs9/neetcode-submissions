class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            meio = int(left + (right - left)/2)
            if nums[meio] == target:
                return meio
            elif target > nums[meio]:
                left = meio + 1
            else:
                right = meio - 1
        
        return -1
