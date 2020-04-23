class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicts = {}
        maxLen = start = 0
        
        for idx, char in enumerate(s):
            if char in dicts:
                nextStart = dicts[char] + 1
                if nextStart > start:
                    start = nextStart
                    
            maxLen = max(maxLen, idx - start + 1)
            dicts[char] = idx
            
        return maxLen
