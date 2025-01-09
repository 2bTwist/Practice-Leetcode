from typing import List

import time
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # #Brute Force:
        # #Time Complexiy: O(n^2) because of the nested for loop
        # #Space Complexity: O(1)
        # mPrice = 0
        # for i in range(len(prices)):

        #     for j in range(i+1, len(prices)):
        #         price = max(mPrice, (prices[j] - prices[i]))
        
        # return mPrice
                
        #Optimal
        #Time Complexity: O(n) Well we just move through the array once
        #Space Complexity: O(1) just pointers are used so no new space
        
        mPrice = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                mPrice = max(mPrice, (prices[r] - prices[l]))
            r += 1
            
        return mPrice

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

            result =  solution.maxProfit(nums)
            
            end_time = time.perf_counter()

            # Measure memory usage after running the function
            final_memory = sys.getsizeof(nums) + sys.getsizeof(result)  # Memory used by 'nums' and 'result'

            full_time = full_time + (end_time-start_time)
            full_memory = (final_memory) + full_memory

            print(f"Input:{nums}, MaxProfit: {result}")
            print(f"Time Taken: {(end_time-start_time)* 10**6:.2f}\u00b5s, Memory Usage:{final_memory}bytes \n")
    
    print(f"***Total Time: {full_time* 10**6:.2f}\u00b5s, Total Memory:{full_memory}bytes")