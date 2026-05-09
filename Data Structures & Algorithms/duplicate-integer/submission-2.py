class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         st=set(nums)
         return False if len(st)==len(nums) else True

#  brute force solution
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]==nums[j]:
#             return True
# return False

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 return True
#         return False

