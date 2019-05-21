class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        disctingMorseCodes = []
        
        for word in words:
            print("------------------")
            wordMorseCode = ""
            for char in word:
                wordMorseCode += morseCodes[ord(char) - 97]
                
            if wordMorseCode not in disctingMorseCodes:
                disctingMorseCodes.append(wordMorseCode)
            
        return len(disctingMorseCodes)
        
