class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         st=set(nums)
         return False if len(st)==len(nums) else True