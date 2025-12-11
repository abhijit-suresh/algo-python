# https://leetcode.com/problems/3sum/description/
## Inward Traversal

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            pairs = self.pair_sum_sorted(nums, i+1, -nums[i])
            for pair in pairs:
                triplets.append([nums[i]] + pair)
        
        return triplets
    
    def pair_sum_sorted(self,nums, start, target):
        pairs = []
        left, right = start, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                pairs.append([nums[left], nums[right]])
                left += 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                    continue
            elif total > target:
                right -= 1
            else:
                left += 1

        return pairs