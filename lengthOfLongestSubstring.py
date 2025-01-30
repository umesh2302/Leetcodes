class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicts = {} # create a dictionary
        substring = "" # create a substring
        for i in range(len(s)):
            if substring == "":
                substring = substring + s[i]
            else:
                if s[i] != 

            dicts