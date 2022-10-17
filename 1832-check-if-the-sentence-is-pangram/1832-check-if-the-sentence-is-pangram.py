class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        bit = 0
        
        for char in sentence:
            bit |= (1 << (ord(char) - ord('a')))
        
        #print(bin(bit))
        return bit == (1 << 26) - 1