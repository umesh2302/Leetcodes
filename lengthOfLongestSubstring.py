class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_string = "" # store the current substring
        longest_string = "" # store the longest substring found so far
        for i in range(len(s)):
            if s[i] in temp_string:
                if len(temp_string) > len(longest_string):
                    longest_string = temp_string
                    
                temp_string = temp_string[temp_string.index(s[i])+1:] + s[i]
            else:
                temp_string = temp_string + s[i]
        
        if len(temp_string) > len(longest_string):
            longest_string = temp_string

        return len(longest_string)
    
# test cases
test = Solution().lengthOfLongestSubstring("vdvev") # 
print(test) # 3
