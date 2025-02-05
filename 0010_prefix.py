## beaten 100% of submissions
#https://leetcode.com/problems/longest-common-prefix/
import typing
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        lengthOfWords = len(strs)
        prefix =""
        for i in range(len(strs[0])): 
            for j in range (1,lengthOfWords):
                if len(strs[j]) >= i+1:
                    if strs[0][i] == strs[j][i]:
                        continue 
                    else :
                        return prefix
                        break
                else :
                    return prefix
                        
            prefix += strs[0][i]
        return prefix
                
# Time complexity: O(n*m) where n is the number of words and m is the length of the word
#test cases
print(Solution().longestCommonPrefix(["flower","flow","flight"])) #fl


            
