class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hist = {}
        for n in range(0, len(nums)):
            diff = target - nums[n]
            hist[nums[n]] = 1

            if (diff in hist) and (nums.index(diff) != n):
                return [nums.index(diff), n]
            