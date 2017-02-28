from Part1 import *
from Part2 import *
import random

class Investor(object):
    def __init__(self, budget, mode, start):
        self.budget = budget
        self.mode = mode
        self.start = start

    def investment_mode(self):
        portfolio = []
        if self.investment_mode == "defensive":
            while self.budget > 0:
                select = random.choice([1000, 3000])
                self.budget = int(self.budget - int(select))
            return portfolio
        if self.investment_mode == "aggressive":
            while self.budget > 0:
                select = random.choice(["AAPL", "GOOGL", "YHOO", "AXP", "XOM", "KO", "NOK", "MS", "IBM", "FDX"])
                self.budget = int(self.budget - int(int(select)*random.choice(0, 0.5 * max(self.budget/int(select['High'])))))
                if self.budget < 100:
                    break
            return portfolio
        if self.investment_mode == "mixed":
            while self.budget > 0:
                select = random.choice(random.choice([1000, 3000]),["AAPL", "GOOGL", "YHOO", "AXP", "XOM", "KO", "NOK", "MS", "IBM", "FDX"])
                If random.choice(random.choice([1000, 3000]) == True:
                    select = random.choice([1000, 3000])
                    self.budget = int(self.budget - int(select))
                Elif
                    select = random.choice(["AAPL", "GOOGL", "YHOO", "AXP", "XOM", "KO", "NOK", "MS", "IBM", "FDX"])
                    self.budget = int(self.budget - int(int(select) * random.choice(0, 0.5 * max(self.budget / int(select['High'])))))
                return portfolio
            else:
                break
