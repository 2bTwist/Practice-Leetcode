#Added this line to allow "List"
from typing import List

import time
import sys

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # #Brute Force
        # #Time Complexity: O(n^2) because of nested for loop
        # #Space Complexity: O(1) because no new value is created
        # for i in range(0, len(nums)):
        #     for j in range((i+1), len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
    
        # #Sub-Optimal
        # #Time Complexity: O(nlogn) because sorting takes logn then going through each item takes n time
        # #Space Complexity: O(1)/O(n) depends on sorting algorithm but no new value is created.
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False

        #Sub-Optimal
        #Time Complexity: O(n) set goes through each item to create a set with no duplicates
        #Space Complexity: O(n) depends on sorting algorithm but no new value is created.
        if len(set(nums)) != len(nums):
            return True
        else:
            return False

if __name__ == "__main__":
    # Creating an instance of Solution
    solution = Solution()

    full_time = 0
    full_memory = 0

    # Open and read file with test cases
    with open("test_cases.txt", "r") as file:
        for number, line in enumerate(file, 1):
            # map does integer casting on every value in each line
            nums = list(map(int, line.strip().split(",")))

            # Measure memory usage before running the function
            initial_memory = sys.getsizeof(nums)  # Memory used by 'nums' list

            start_time = time.perf_counter()

            result =  solution.hasDuplicate(nums)
            
            end_time = time.perf_counter()

            # Measure memory usage after running the function
            final_memory = sys.getsizeof(nums) + sys.getsizeof(result)  # Memory used by 'nums' and 'result'

            full_time = full_time + (end_time-start_time)
            full_memory = (final_memory) + full_memory

            print(f"Case 1:{nums} = {result}")
            print(f"Time Taken: {(end_time-start_time)* 10**6:.2f}\u00b5s, Memory Usage:{final_memory}bytes \n")
    
    print(f"***Total Time: {full_time* 10**6:.2f}\u00b5s, Total Memory:{full_memory}bytes")