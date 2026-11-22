class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while i<j:
            val = numbers[i] + numbers[j]
            if val == target:
                return [i+1, j+1]
            elif val>target:
                j -= 1
            else:
                i += 1
        return [-1, -1]