# pcost.py
#
# Exercise 1.27


import csv
import sys
import report


def portfolio_cost(filename, select=None, types=None):
    """Computes the total cost (shares*price) of a portfolio file."""
    rows = report.read_portfolio(filename, select=select, types=types)
    total_cost = 0
    for rowno, row in enumerate(rows, start=1):
        try:
            total_cost += row["shares"] * row["price"]
        except ValueError:
            print(f"Row {rowno}: Bad row: {row}")
    return total_cost


def main(argv):
    cost = None
    if len(argv) != 2:
        cost = portfolio_cost(
            "Data/portfolio.csv",
            select=["name", "shares", "price"],
            types=[str, int, float],
        )
    else:
        cost = portfolio_cost(
            argv[1], select=["name", "shares", "price"], types=[str, int, float]
        )
    print(f"Total Cost: ${cost:.2f}")


if __name__ == "__main__":
    import sys

    main(sys.argv)
