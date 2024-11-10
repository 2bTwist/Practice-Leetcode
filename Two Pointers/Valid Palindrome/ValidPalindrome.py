import time
import sys

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #Sub-Optimal
        # #Sub-Optimal
        # #Time Complexity: O(n) because it goes through every character in s
        # #Space Complexity: compares with a newly created, reverted string
        pal = ""

        for i in s:
            if i.isalnum():
                pal = pal + i.lower()
                # or pal += i.lower()

        #[::-1] is just a python method to revert strings
        return pal == pal[::-1]

if __name__ == "__main__":
    # Creating an instance of Solution
    solution = Solution()

    full_time = 0
    full_memory = 0

    # Open and read file with test cases
    with open("test_cases.txt", "r") as file:
        for number, line in enumerate(file, 1):
            # map does integer casting on every value in each line
            nums = line.strip()

            # Measure memory usage before running the function
            initial_memory = sys.getsizeof(nums)  # Memory used by 'nums' list

            start_time = time.perf_counter()

            result =  solution.isPalindrome(nums)
            
            end_time = time.perf_counter()

            # Measure memory usage after running the function
            final_memory = sys.getsizeof(nums) + sys.getsizeof(result)  # Memory used by 'nums' and 'result'

            full_time = full_time + (end_time-start_time)
            full_memory = (final_memory) + full_memory

            print(f"String:{nums} = {result}")
            print(f"Time Taken: {(end_time-start_time)* 10**6:.2f}\u00b5s, Memory Usage:{final_memory}bytes \n")
    
    print(f"***Total Time: {full_time* 10**6:.2f}\u00b5s, Total Memory:{full_memory}bytes")