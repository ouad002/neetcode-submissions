class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        for i in range(n):
            cpl= target - nums[i]
            if cpl in seen:
                return [seen[cpl], i]
            seen[nums[i]]=i
        