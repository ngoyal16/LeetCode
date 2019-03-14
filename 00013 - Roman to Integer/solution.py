class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        arr = list(s[::-1])
        n = len(arr)
        sum = symbol[arr[0]]
        
        for i in range(1, n):
            if (symbol[arr[i - 1]] > symbol[arr[i]]) :
                sum = sum - symbol[arr[i]]
            else:
                sum = sum + symbol[arr[i]]
            
        
        return sum
