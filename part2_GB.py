#Part 2, Grace Bryant
#Given list of predicted stock prices by day
#Choose one day to buy and one day to sell
#Return maximum profit or 0 if not possible to profit/gain
prices = input().split(",")
n = len(prices)

def stock_trade(price):
    #Exception if only 1 number entered
    if (n == 1):
        return 0

    buy = []
    sell = []
    profit = []
    x = 0

    #Can't sell on day 1, can't buy on final (nth) day
    for i in range(0, n-1):
        buy.append(price[i])

    for i in range(1, n):
        sell.append(price[i])

    buy = [int(i) for i in buy]
    sell = [int(j) for j in sell]

    #Check maximum possible difference between days; accounting that
    #it is not possible to sell before buying
    for i in range(0, len(buy)):
        for j in range(0, len(sell)):
            if j > i:
              x = sell[j] - buy[i]
              profit.append(x)

    #Return maximum possible profit
    optimal = max(profit)

    #if profit is negative, instead return 0 (do not buy/sell)
    if(optimal < 0):
        optimal = 0

    return optimal

print(stock_trade(prices))

