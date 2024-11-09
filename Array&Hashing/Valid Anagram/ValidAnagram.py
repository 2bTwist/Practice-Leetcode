import time
import sys

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Edge Case: If s and t are not of thesame length of strings
        if len(s) != len(t):
            return False
        
        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

        for key in s_dict:
            if s_dict.get(key) != t_dict.get(key):
                return False
        
        return True