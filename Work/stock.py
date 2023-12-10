# stock.py

from typedproperty import String, Integer, Float


class Stock:
    """
    An instance of a stock holding consisting of name, shares, and price.
    """

    # Note: __slots__ is most commonly used as an optimization on classes that serve as data structures.
    # Using slots will make such programs use far-less memory and run a bit faster.
    # __slots__ = ("name", "shares", "price")

    name = String("name")
    shares = Integer("shares")
    price = Float("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"

    @property
    def cost(self):
        """
        Return the cost as shares*price
        """
        return self.shares * self.price

    def sell(self, nshares):
        """
        Sell a number of shares
        """
        self.shares -= nshares
