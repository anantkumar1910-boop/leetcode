class Solution:
    def twoSum(self, nums, target):
        for a in range(len(nums)):
            dif = target - nums[a]
            if dif in nums:
                if nums.index(dif) == a:
                    continue
                return [a, nums.index(dif)]
        return []