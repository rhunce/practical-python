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

Data/missing.csv
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",,70.44
"""

import csv
import sys


def portfolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file."""
    total_cost = 0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                n_shares = int(record["shares"])
                price = float(record["price"])
                total_cost += n_shares * price
            except ValueError:
                print(f"Row {rowno}: Bad row: {row}")

        return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"


# cost = portfolio_cost(filename)
# cost = portfolio_cost("Data/missing.csv")
cost = portfolio_cost("Data/portfoliodate.csv")
print(f"Total Cost: ${cost:.2f}")
