# https://leetcode.com/problems/coin-change/

def coinChange(coins, amount):
  coins = sorted(coins)
  table = [[x for x in range(amount + 1)] for y in range(len(coins))]
  
  for coinIdx in range(len(coins)):
    coin = coins[coinIdx]
    for a, amount in enumerate(table[coinIdx]):
      minimum = -1
      remainder = amount % coin
      if amount < coin:
        minimum = table[coinIdx - 1][a] if table[coinIdx - 1][a] is not None else 0
      elif remainder == 0:
        minimum = amount // coin
      elif coinIdx >= 1:
        remainderMinCoins = table[coinIdx - 1][remainder]
        floorDivisionMinCoins = amount // coin
        minimum = remainderMinCoins + floorDivisionMinCoins
      table[coinIdx][a] = minimum
  return table[-1][-1]


# result = coinChange([1, 2, 5], 11)
result = coinChange([3, 5, 1], 23)
print(result)
