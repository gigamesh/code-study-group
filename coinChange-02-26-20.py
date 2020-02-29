# https://leetcode.com/problems/coin-change/

def coinChange(coins, amount):
  table = [[x for x in range(amount + 1)] for y in range(len(coins))]
  
  for coinIdx in range(len(coins)):
    coin = coins[coinIdx]
    for a, amount in enumerate(table[coinIdx]):
      minimum = 0
      remainder = amount % coin
      if amount < coin:
        minimum = table[coinIdx - 1][a] if table[coinIdx - 1][a] is not None else 0
      elif remainder == 0:
        minimum = amount // coin
      else:
        remainderMinCoins = table[coinIdx - 1][a - remainder]
        floorDivisionMinCoins = amount // coin
        minimum = remainderMinCoins + floorDivisionMinCoins
        print('coin: ', coin, '; amount: ', amount, '; remainderMinCoins: ', remainderMinCoins, '; floorDivisionMinCoins: ', floorDivisionMinCoins)
      table[coinIdx][a] = minimum
  print(table)
  return table[-1][-1]


result = coinChange([1, 2, 5], 10)
print(result)
