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

if __name__ == "__main__":
    # Example input list
    test_nums = [1, 2, 3, 4, 1]
    
    # Creating an instance of Solution
    solution = Solution()
    
    # Call the function and print the result
    result = solution.hasDuplicate(test_nums)
    print("Contains duplicate:", result)