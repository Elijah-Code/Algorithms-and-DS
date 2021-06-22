"""
GeeksForGeeks

https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
"""

def knapsack(values, weights, max_capacity, ix=0):
    if ix >= len(values) or max_capacity <= 0:
        return 0
    
    take = 0
    if max_capacity >= weights[ix]:
        take = values[ix] + knapsack(values, weights, max_capacity-weights[ix], ix)

    without = knapsack(values, weights, max_capacity, ix+1)

    return max(take, without)
    

values = [1,100,30, 500]
weights = [10,20,30, 10]
capacity = 50

best_value = knapsack(values, weights, capacity)
print(best_value)