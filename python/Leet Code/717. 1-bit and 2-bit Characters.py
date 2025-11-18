import logging

logging.basicConfig(level=logging.INFO)
class Solution(object):
    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0
    
sol=Solution()
logging.info(sol.isOneBitCharacter([1,0,0,1]))