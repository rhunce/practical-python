# report.py
#
# Exercise 2.4

import csv
from pprint import pprint


def read_portfolio(filename):
    """Opens a given portfolio file and reads it into a list of dictionaries."""
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    """Opens a given prices file and reads it into a list of dictionaries."""
    prices = {}

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print("Skipping empty row...")

    return prices


def compute_gain(filename1, filename2):
    total_gain = 0
    portfolio = read_portfolio(filename1)
    prices = read_prices(filename2)
    for holding in portfolio:
        stock = holding["name"]
        cost_basis = holding["price"] * holding["shares"]
        current_value = prices[stock] * holding["shares"]
        stock_gain = current_value - cost_basis
        total_gain += stock_gain
    return total_gain
