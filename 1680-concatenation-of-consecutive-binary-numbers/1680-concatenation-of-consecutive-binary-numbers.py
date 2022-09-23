class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        return int("".join(bin(x)[2:] for x in range(1, n+1)), 2)%(1000000000 + 7)