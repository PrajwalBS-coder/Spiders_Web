class Solution(object):
    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0
    
sol=Solution()
print(sol.isOneBitCharacter([1,0,0,1]))