prices = [7,1,5,3,6,4]
profit = 0
mini=prices[0]
for i in range(1, len(prices)):
    cost=0
    cost=prices[i]-mini
    profit=max(cost, profit)
    mini=min(mini, prices[i])
print(profit)