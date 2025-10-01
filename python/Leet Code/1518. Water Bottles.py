numBottles = 15
numExchange = 4
consumed_bottles = 0
# while numBottles >= numExchange:
#     consumed_bottles += numExchange
#     numBottles -= numExchange
#     numBottles += 1
# print(numBottles+consumed_bottles)
print(numBottles+(numBottles-1)//(numExchange-1))#Here the fist op is (numBottles-1)//(numExchange-1) which will  return the value of the add with numBottles

