

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts={}
        for i in range(len(nums)):
            if target-nums[i] in dicts:
                return [dicts[target-nums[i]],i]
            dicts[nums[i]]=i
        return []


Solution().twoSum([2, 8, 21, 15,7], 9) 
print (Solution().twoSum([2, 8, 21, 15,7], 9))