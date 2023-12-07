# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    """Opens a given portfolio file and reads it into a list of tuples."""
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(holding)
    return portfolio
