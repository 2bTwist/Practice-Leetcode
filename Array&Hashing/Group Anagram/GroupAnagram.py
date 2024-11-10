from typing import  List
from collections import defaultdict #need this to use defaultdict

import time
import sys

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # #Sub-Optimal
        # #Time Complexity: O(m * nlogn) m is the amount of items, sorts in logn for each value for n(length of strings)
        # #Space Complexity: O(m*n)
        # sorted_dict = {}
        # output = []

        # for i in strs:
        #     val = ''.join(sorted(i))
        #     if val not in sorted_dict:
        #         sorted_dict[val] = [i]
        #     else:
        #         sorted_dict[val].append(i)

        # for value in sorted_dict.values():
        #    output.append(value)

        # return output

        #Optimal
        #Time Complexity: O(m * nlogn) m is the amount of items, sorts in logn for each value for n(length of strings)
        #Space Complexity: O(m*n)
        res = defaultdict(list)

        for i in strs:
            count = [0] * 26 #maximum number of alpahabets for each word

            for c in i:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(i)
        
        return list(res.values())


        

if __name__ == "__main__":
    # Creating an instance of Solution
    solution = Solution()

    full_time = 0
    full_memory = 0

    # Open and read file with test cases
    with open("test_cases.txt", "r") as file:
        for number, line in enumerate(file, 1):
            # map does integer casting on every value in each line
            nums = list(line.strip().split(","))

            # Measure memory usage before running the function
            initial_memory = sys.getsizeof(nums)  # Memory used by 'nums' list

            start_time = time.perf_counter()

            result =  solution.groupAnagrams(nums)
            
            end_time = time.perf_counter()

            # Measure memory usage after running the function
            final_memory = sys.getsizeof(nums) + sys.getsizeof(result)  # Memory used by 'nums' and 'result'

            full_time = full_time + (end_time-start_time)
            full_memory = (final_memory) + full_memory

            print(f"Stream:{nums} | Output:= {result}")
            print(f"Time Taken: {(end_time-start_time)* 10**6:.2f}\u00b5s, Memory Usage:{final_memory}bytes \n")
    
    print(f"***Total Time: {full_time* 10**6:.2f}\u00b5s, Total Memory:{full_memory}bytes")