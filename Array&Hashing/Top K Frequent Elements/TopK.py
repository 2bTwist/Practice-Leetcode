#Added this line to allow "List"
from typing import List

import time
import sys

class Solution:

    # #Sub-Optimal
    # #Time Complexity: O(nlogn), logn because of the sorting algorithm
    # #Space Complexity: O(n)
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = {}
    #     output = []

    #     for i in nums:
    #         count[i] = 1 + count.get(i, 0)

    #     for num, freq in count.items():
    #         output.append([freq, num])
        
    #     output.sort()

    #     result = []
    #     for i in range(k):
    #         result.append(output.pop()[1])

    #     return result

    #Time Complexity: O(n)
    #Space Complexity: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


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

            result =  solution.topKFrequent(nums[:-1], nums[-1])
            
            end_time = time.perf_counter()

            # Measure memory usage after running the function
            final_memory = sys.getsizeof(nums) + sys.getsizeof(result)  # Memory used by 'nums' and 'result'

            full_time = full_time + (end_time-start_time)
            full_memory = (final_memory) + full_memory

            print(f"Numbers:{nums[:-1]}, k:{nums[-1]} = {result}")
            print(f"Time Taken: {(end_time-start_time)* 10**6:.2f}\u00b5s, Memory Usage:{final_memory}bytes \n")
    
    print(f"***Total Time: {full_time* 10**6:.2f}\u00b5s, Total Memory:{full_memory}bytes")