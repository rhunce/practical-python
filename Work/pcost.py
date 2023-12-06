# pcost.py
#
# Exercise 1.27

"""
Data/portfolio.csv

name,       shares,     price
"AA",       100,        32.20
"IBM",      50,         91.10
"CAT",      150,        83.44
"MSFT",     200,        51.23
"GE",       95,         40.37
"MSFT",     50,         65.10
"IBM",      100,        70.44

"""

with open("Data/portfolio.csv", "rt") as f:
    headers = next(f)
    cost = 0
    for line in f:
        stock_info = line.split(",")
        shares = int(stock_info[1])
        price = float(stock_info[2])
        cost += shares * price

    print(f"Total Cost: ${cost:.2f}")
