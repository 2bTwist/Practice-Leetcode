from typing import List

import time
import sys

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute Force
        #Time Complexity: O(n^2) because of nested for loop
        #Space Complexity: O(1) because no new value is created
        index = []
        for i in range (len(nums)):
            pair =  target - nums[i]
            for j in range (len(nums)):
                if (nums[j] == pair) and (i != j):
                    index.append(i)
                    index.append(j)
                    return index

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

            result =  solution.twoSum(nums[:-1], nums[-1])
            
            end_time = time.perf_counter()

            # Measure memory usage after running the function
            final_memory = sys.getsizeof(nums) + sys.getsizeof(result)  # Memory used by 'nums' and 'result'

            full_time = full_time + (end_time-start_time)
            full_memory = (final_memory) + full_memory

            print(f"Input:{nums[:-1]}, Target:{nums[-1]} = {result}")
            print(f"Time Taken: {(end_time-start_time)* 10**6:.2f}\u00b5s, Memory Usage:{final_memory}bytes \n")
    
    print(f"***Total Time: {full_time* 10**6:.2f}\u00b5s, Total Memory:{full_memory}bytes")