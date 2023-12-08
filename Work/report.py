# report.py
#
# Exercise 2.4

import csv
import fileparse


def read_portfolio(filename):
    """Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price."""
    return fileparse.parse_csv(filename, types=[str, int, float])


def read_prices(filename):
    """Opens a given prices file and reads it into a list of dictionaries."""
    return dict(fileparse.parse_csv(filename, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    """Makes a report of stocks in portfolio with the shares owned, current price, and share gain/loss."""
    report = []
    for holding in portfolio:
        stock = holding["name"]
        n_shares = holding["shares"]
        current_price = prices[stock]
        share_appreciation = current_price - holding["price"]
        report.append((stock, n_shares, current_price, share_appreciation))
    return report


def print_report(report):
    """Prints a report of stocks in portfolio with the shares owned, current price, and share gain/loss."""
    headers = ("Name", "Shares", "Price", "Change")
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(("-" * 10 + " ") * len(headers))
    for name, shares, price, change in report:
        formatted_price = f"${price:.2f}"
        print(f"{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}")
    # ALTERNATIVE
    # for r in report:
    #     print("%10s %10d %10.2f %10.2f" % r)


def portfolio_report(
    portfolio_filename="Data/portfolio.csv", prices_filename="Data/prices.csv"
):
    """Prints a report of stocks in portfolio with the shares owned, current price, and share gain/loss."""
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report("Data/portfolio.csv", "Data/prices.csv")
