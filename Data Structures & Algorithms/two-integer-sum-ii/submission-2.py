class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hist = {}

        for n in range(0, len(numbers)):
            diff = target - numbers[n]
            if diff in hist:
                return [hist[diff], n+1]
            else:
                hist[numbers[n]] = n+1
              