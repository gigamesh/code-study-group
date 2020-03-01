# https://www.algoexpert.io/questions/Knapsack%20Problem
import pprint

def knapsackProblem(items, capacity):
  knapValues = [[{'value': 0, 'indices': []} for x in range(capacity + 1)] for y in range(len(items))]
  for i in range(len(knapValues)):
    value, weight = items[i]
    for currentCap in range(len(knapValues[i])):
      # check if this item can fit in current capacity
      if weight <= currentCap:
        # if it can fit and their is a remainder, then cache the remainder value & remainder indices
        remainder = currentCap - weight
        if i > 0:
          previousMax = knapValues[i - 1][currentCap]
          currentMax = knapValues[i][currentCap]
          if remainder > 0:
            remainderMax = knapValues[i - 1][remainder]
            currentMax['value'] += remainderMax['value']
            currentMax['indices'] += remainderMax['indices']
          currentMax['value'] += value
          currentMax['indices'].append(i)
          sortedMaxes = sorted([currentMax, previousMax], key= lambda choice: choice['value'])
          knapValues[i][currentCap] = sortedMaxes[-1]
        else:  
          knapValues[i][currentCap]['value'] += value
          knapValues[i][currentCap]['indices'].append(i)
      elif i > 0:
        knapValues[i][currentCap]['value'] += knapValues[i - 1][currentCap]['value']
        knapValues[i][currentCap]['indices'] += knapValues[i - 1][currentCap]['indices']

  pprint.pprint(knapValues)
  return list(knapValues[-1][-1].values())

# result = knapsackProblem([[1,2],[4,3],[5,6],[6,7]], 10)
result = knapsackProblem([[2,1],[70,70],[30,30],[69,69],[100,100]], 100)

print(result)