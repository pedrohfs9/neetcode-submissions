class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hist = {}

        for n in range(0, len(nums)):
            if nums[n] in hist:
                if abs(hist[nums[n]] - n) <= k:
                    return True
                hist[nums[n]] = n
            else:
                hist[nums[n]] = n

        return False
