import time
import sys

class Solution:
    def isValid(self, s: str) -> bool:
        # #Brute Force
        # #Time Complexity: O(n^2) 
        # #Space Complexity: O(n) compares with a newly updated string
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        # return s == ''
    
        #Optimal (This is my personal)
        #Time Complexity: O(n) 
        #Space Complexity: O(n) compares with a newly updated stack array
        stack = []

        for i in s:
            if i == ")":
                if len(stack) == 0:
                    return False
                if stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif i == "]":
                if len(stack) == 0:
                    return False
                if stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            elif i == "}":
                if len(stack) == 0:
                    return False
                if stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0

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

            result =  solution.isValid(nums)
            
            end_time = time.perf_counter()

            # Measure memory usage after running the function
            final_memory = sys.getsizeof(nums) + sys.getsizeof(result)  # Memory used by 'nums' and 'result'

            full_time = full_time + (end_time-start_time)
            full_memory = (final_memory) + full_memory

            print(f"String:{nums} = {result}")
            print(f"Time Taken: {(end_time-start_time)* 10**6:.2f}\u00b5s, Memory Usage:{final_memory}bytes \n")
    
    print(f"***Total Time: {full_time* 10**6:.2f}\u00b5s, Total Memory:{full_memory}bytes")