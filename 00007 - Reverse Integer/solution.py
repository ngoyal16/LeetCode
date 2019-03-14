class Solution:
    def reverse(self, x: int) -> int:
        isNegative = x < 0
        
        if (isNegative):
            x = x * -1
            
        s = str(x)
        rev = int(s[::-1])
        
        if (isNegative):
            if (rev > 2147483648) :
                return 0
            
            rev = rev * -1
        
        if (rev > 2147483647) :
            return 0
        
        return rev
