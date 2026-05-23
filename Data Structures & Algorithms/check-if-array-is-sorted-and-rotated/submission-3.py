# Sorted + rotated array → only one breaking point.
# More than one break → not valid.
# We loop once through array
# O(n) time
# O(1) space
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count += 1
        return count <= 1