# https://leetcode.com/problems/coin-change/

def coinChange(coins, amount):
  table = [[x for x in range(amount + 1)] for y in range(len(coins))]
  
  for r, row in enumerate(table):
    coin = coins[r]
    for amount in row:
      print(coin)

coinChange([1, 2, 5], 10)
