#Part 1; Grace Bryant
#Find total value of a portfolio across multiple items and shares
#Values stored in JSON file

import json
import pandas as pd

#Open JSON file
f = open('stocks.json')
data = json.load(f)

#Portfolio passed to application in format "TICKER:QTY"
#Parse input portfolio and separate into stock name and qty
portfolio = input().split(",")

def portfolio_value(port):
    tick = []
    qty = []
    price = []
    values = []

    for i in range(0, len(port)):
        new = port[i].split(":")
        tick.append(new[0])
        qty.append(new[1])

    qty = [int(i) for i in qty]

    #Find value of each stock in JSON file
    #Convert to dataframe
    df = pd.DataFrame(data)
    ticker = df['ticker'].tolist()
    close = df['close'].tolist()

    for i in range(0, len(tick)):
        for j in range(0, len(ticker)):
            if tick[i] == ticker[j]:
                price.append(close[j])
                break

    #Return total value of portfolio
    #Multiply qty of shares owned by value of share at close, then sum
    for i in range(0, len(tick)):
        value = price[i]*qty[i]
        values.append(value)

    port_val = sum(values)
    return port_val

print(portfolio_value(portfolio))

#Close JSON file when done
f.close()