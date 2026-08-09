# Best time to buy and sell
# O(n^2)
def max_profit(prices):
    profit = 0
    for index, i in enumerate(prices):
        for j in prices[index+1:]:
            if j - i > profit:
                profit = j - i
    return profit

# O(n)
def max_profit_sol(prices):
    min_price = 10000
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

"""
print(max_profit([3, 2, 6, 5, 0, 3]))
print(max_profit([8, 6, 5, 2, 1]))
print(max_profit([1,2]))
"""