class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        count = 0
        charCount = {}
        checkFor1 = []
        checkFor2 = []
        
        for a, b in zip(A, B):
            if (a != b):
                count += 1
                if b in checkFor1 and a in checkFor2:
                    checkFor1.remove(b)
                    checkFor2.remove(a)
                else:
                    checkFor1.append(a)
                    checkFor2.append(b)
            else:
                if a in charCount:
                    charCount[a] += 1
                else:
                    charCount[a] = 1
                    
        if count == 2 and len(checkFor1) == 0 and len(checkFor2) == 0:
            return True
        
        if count == 0:
            for key in charCount:
                if charCount[key] > 1:
                    return True
        
        return False
