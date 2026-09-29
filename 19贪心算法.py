def max_profit(prices):
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i] > prices[i+1]:
            profit += prices[i] - prices[i+1]

    return profit

print(max_profit([7,1,5,3,6,4]))



'''优化'''

def max_profit(prices):
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i+1]:           # 今天比明天便宜
            profit += prices[i+1] - prices[i] # 赚上涨的差价
    return profit

print(max_profit([7, 1, 5, 3, 6, 4]))  # 7
print(max_profit([1, 2, 3, 4, 5]))     # 4
print(max_profit([7, 6, 5, 4, 3, 2]))  # 0