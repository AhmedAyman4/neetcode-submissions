from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums, L, M, R):
            left = nums[L:M+1]
            right = nums[M+1:R+1]

            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def mergeSort(nums, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            mergeSort(nums, l, m)
            mergeSort(nums, m + 1, r)
            merge(nums, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums
