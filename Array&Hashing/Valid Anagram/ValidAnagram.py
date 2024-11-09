import time
import sys

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Edge Case: If s and t are not of thesame length of strings
        if len(s) != len(t):
            return False

        # #Sub-Optimal
        # #Time Complexity: O(nlogn) sorts in logn then compares each value for n
        # #Space Complexity: O(1) or O(n) because of sorting algorithm
        # return sorted(s) == sorted(t)

        #Optimal
        #Time Complexity: O(n) adds each value in s and t too dictionaries, thus n
        #Space Complexity: O(1)        
        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

        for key in s_dict:
            if s_dict.get(key) != t_dict.get(key):
                return False
        # or simply
        # return s_dict == t_dict
        return True

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

            result =  solution.isAnagram(nums[0], nums[1])
            
            end_time = time.perf_counter()

            # Measure memory usage after running the function
            final_memory = sys.getsizeof(nums) + sys.getsizeof(result)  # Memory used by 'nums' and 'result'

            full_time = full_time + (end_time-start_time)
            full_memory = (final_memory) + full_memory

            print(f"s:{nums[0]}, t:{nums[1]} = {result}")
            print(f"Time Taken: {(end_time-start_time)* 10**6:.2f}\u00b5s, Memory Usage:{final_memory}bytes \n")
    
    print(f"***Total Time: {full_time* 10**6:.2f}\u00b5s, Total Memory:{full_memory}bytes")