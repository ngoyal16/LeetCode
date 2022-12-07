class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0":
            return b

        if b == "0":
            return a

        carry = 0
        
        aLen = len(a)
        bLen = len(b)

        maxLen = max(aLen, bLen)

        a = a.zfill(maxLen)
        b = b.zfill(maxLen)

        res = []

        while (maxLen > 0):
            maxLen -= 1

            if a[maxLen] > "0":
                carry += 1

            if b[maxLen] > "0":
                carry += 1

            res.append(str(carry % 2))
            
            carry = carry // 2

        res.append(str(carry))
        
        return "".join(res[::-1]).lstrip("0")
