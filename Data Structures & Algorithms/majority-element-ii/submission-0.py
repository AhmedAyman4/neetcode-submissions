class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        result = []

        for n in nums:
            counter[n]+=1

        for k , v in counter.items():
            if v > len(nums)/3:
                result.append(k)
        return result