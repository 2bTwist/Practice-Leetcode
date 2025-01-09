#Added this line to allow "List"
from typing import List

import time
import sys

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for i in strs:
            result = str(len(i)) + "#" + i + result

        return result

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0

        while i < len(s):
            j = i #Pointer
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length

            final.append(s[i:j])

            i = j

        return final

if __name__ == "__main__":
    # Creating an instance of Solution
    solution = Solution()

    full_time = 0
    full_memory = 0

    # Open and read file with test cases
    with open("test_cases.txt", "r") as file:
        for number, line in enumerate(file, 1):
            # map does integer casting on every value in each line
            nums = list(line.strip().split(", "))

            # Measure memory usage before running the function
            initial_memory = sys.getsizeof(nums)  # Memory used by 'nums' list

            start_time = time.perf_counter()

            encoded =  solution.encode(nums)
            
            decoded = solution.decode(encoded)
            
            end_time = time.perf_counter()

            # Measure memory usage after running the function
            final_memory = sys.getsizeof(nums) + sys.getsizeof(encoded) + sys.getsizeof(decoded) # Memory used by 'nums' and 'result'

            full_time = full_time + (end_time-start_time)
            full_memory = (final_memory) + full_memory

            print(f"Input:{nums}, \nEncoded:{encoded} | Decoded:{decoded}")
            print(f"Time Taken: {(end_time-start_time)* 10**6:.2f}\u00b5s, Memory Usage:{final_memory}bytes \n")
    
    print(f"***Total Time: {full_time* 10**6:.2f}\u00b5s, Total Memory:{full_memory}bytes")