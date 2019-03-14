class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = ""
        
        if len(strs):
            longestPrefix = strs.pop(0)
        
        for s1 in strs:
            n = min(len(longestPrefix), len(s1))
            
            newLongestPrefix = ""
            for i in range(n):
                if longestPrefix[i] == s1[i]:
                    newLongestPrefix = newLongestPrefix + s1[i]
                else:
                    break
                    
            if newLongestPrefix == "":
                return ""
            
            longestPrefix = newLongestPrefix
        return longestPrefix
        
