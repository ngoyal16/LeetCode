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
        
        arr = [symbol[c] for c in s]
        
        n = len(arr)
        sum = arr[n - 1]
        
        # print(arr)
        for i in range(n - 2, -1, -1):
            # print(i, arr[i])
            val = arr[i]
            if (arr[i + 1] > val) :
                sum = sum - val
            else:
                sum = sum + val
            
        return sum
