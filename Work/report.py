# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    """Opens a given portfolio file and reads it into a list of dictionaries."""
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = dict(zip(headers, row))
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


def make_report(portfolio, prices):
    """Makes a report of stocks in portfolio with the shares owned, current price, and share gain/loss."""
    report = []
    for holding in portfolio:
        stock = holding["name"]
        n_shares = int(holding["shares"])
        current_price = prices[stock]
        share_appreciation = float(current_price) - float(holding["price"])
        report.append((stock, n_shares, current_price, share_appreciation))
    return report


def print_report(filename1="Data/portfolio.csv", filename2="Data/prices.csv"):
    """Prints a report of stocks in portfolio with the shares owned, current price, and share gain/loss."""
    portfolio = read_portfolio(filename1)
    prices = read_prices(filename2)
    report = make_report(portfolio, prices)
    headers = ("Name", "Shares", "Price", "Change")
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print("---------- ---------- ---------- -----------")
    for name, shares, price, change in report:
        formatted_price = f"${price:.2f}"
        print(f"{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}")
    # ALTERNATIVE
    # for r in report:
    #     print("%10s %10d %10.2f %10.2f" % r)
