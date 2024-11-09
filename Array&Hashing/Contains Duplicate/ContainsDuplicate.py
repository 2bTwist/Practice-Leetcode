#Added this line to allow "List"
from typing import List

import time

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
    # Creating an instance of Solution
    solution = Solution()

    full_time = 0

    # Open and read file with test cases
    with open("test_cases.txt", "r") as file:
        for number, line in enumerate(file, 1):
            # map does integer casting on every value in each line
            nums = list(map(int, line.strip().split(",")))

            start_time = time.perf_counter()

            result =  solution.hasDuplicate(nums)
            
            end_time = time.perf_counter()

            full_time = full_time + (end_time-start_time)

            print(f"Case 1:{nums} = {result}")
            print(f"Time Taken: {(end_time-start_time)* 10**6:.2f}\u00b5s \n")
    
    print(f"Total Time: {full_time* 10**6:.2f}\u00b5s")