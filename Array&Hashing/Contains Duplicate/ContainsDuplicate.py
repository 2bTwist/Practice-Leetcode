#Added this line to allow "List"
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Brute Force
        #Time Complexity: O(n^2)
        #Space Complexity: O(1)
        for i in range(0, len(nums)):
            for j in range((i+1), len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False    