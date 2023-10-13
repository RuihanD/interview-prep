"""
Write a function that returns a random stock pick from a given list of stocks.
The random function cannot return a stock pick that has already been returned until the list is exhausted. Repeat the process.

Follow-up: when adding a stock to the pool, the stock needs to wait a generation to be eligible for random generation.
i.e. if "appl" is added to the pool, it needs to wait until one random function is called to be a valid return value
"""
from random import randint
class RandomStockGenerator:
    def __init__(self):
        self.stocks = []
        self.reAdd = []
        self.removed = set()

    # Adds a stock for consideration. It can be picked
    # by the random function immediately unless it's removed.
    # Assumes the stock isn't already in the list. O(1)
    def add(self, name):
        if name in self.removed:
            self.removed.remove(name)
        else:
            self.stocks.append(name)

    # Removes a stock from consideration whether it has
    # already been picked or not. Doesn't consider it again
    # after we remove it. Assumes the stock was
    # previously added. O(1)
    def remove(self, name):
        self.removed.add(name)

    # Returns a random stock, doesn't pick it again
    # until all stocks have been picked at least once.
    # Assumes there is at least one stock to pick.
    # O(1) amortized worst-case time; we can only "re-pick"
    # as many times as we remove elements.
    # Individual call worst case is O(N).
    def random(self):
        res = None
        while res is None:
            if len(self.stocks) == 0:
                self._flush()

            ri = randint(0, len(self.stocks) - 1)
            name = self.stocks[ri]
            self.stocks[ri], self.stocks[-1] = self.stocks[-1], self.stocks[ri]
            self.stocks.pop()
            if name in self.removed:
                self.removed.remove(name)
            else:
                self.reAdd.append(name)
                res = name

        return res

    # Call this when stocks is empty. For each stock we've
    # previously picked, add it back to the stocks array,
    # unless it was previously removed. In which case,
    # don't add it back.
    def _flush(self):
        while self.reAdd:
            name = self.reAdd.pop()
            if name in self.removed:
                self.removed.remove(name)
            else:
                self.stocks.append(name)
