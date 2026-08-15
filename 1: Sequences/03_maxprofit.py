"""
You are given an array prices where prices[i] is the price of a given stock on the 
ith day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you 
cannot achieve any profit, return 0.

Example 1:
Input: [3, 2, 6, 5, 0, 3]
Expected Output: 4
Justification: Buy the stock on day 2 (price = 2) and sell it on day 3 (price = 6). Profit = 6 - 2 = 4.

Example 2:
Input: [8, 6, 5, 2, 1]
Expected Output: 0
Justification: Prices are continuously dropping, so no profit can be made.

Example 3:
Input: [1, 2]
Expected Output: 1
Justification: Buy on day 1 (price = 1) and sell on day 2 (price = 2). Profit = 2 - 1 = 1.
Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

def max_profit(prices):
    profit = 0
    for index, price in enumerate(prices):
        for later_price in prices[index+1:]:
            if later_price - price > profit:
                profit = later_price - price
    return profit

# O(n)
def max_profit_sol(prices):
    min_price = 10000
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Test:
print(max_profit([3, 2, 6, 5, 0, 3]))
print(max_profit([8, 6, 5, 2, 1]))
print(max_profit([1,2]))
