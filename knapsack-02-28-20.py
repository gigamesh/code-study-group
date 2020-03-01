# https://www.algoexpert.io/questions/Knapsack%20Problem

def knapsackProblem(items, capacity):
  template = {'value': 0, 'indices': []}
  knapValues = [[template for x in range(capacity + 1)] for y in range(len(items) + 1)]
  for i in range(len(knapValues)  - 1):
    value, weight = items[i]
    for currentCap in range(len(knapValues[i])):
      # check if this item can fit in current capacity
      if weight <= currentCap:
        # if it can fit and their is a remainder, then cache the remainder value & remainder indices
        if currentCap % weight > 0:
          remainder = currentCap - weight
          remainderMax = knapValues[i - 1][remainder]
          if remainderMax['value'] > 0:
            knapValues[i][currentCap]['value'] += remainderMax['value']
            knapValues[i][currentCap]['indices'] += remainderMax['indices']
        else:
         # if there is no remainder, add the current value & cache the index
          knapValues[i][currentCap]['value'] += value
          knapValues[i][currentCap]['indices'].append(i)
  return knapValues
  # return list(knapValues[-1][-1].values())

	
result = knapsackProblem([[1,2],[4,3],[5,6],[6,7]], 10)

print(result)