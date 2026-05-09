class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        nums_set = set(sorted_nums)
        flag = True
        for i in range(1,len(nums_set)+1):
            if i not in nums_set:
                flag = False
                return i
        if flag:
            return max(nums)+1