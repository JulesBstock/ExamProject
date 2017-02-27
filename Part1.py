import matplotlib.pyplot as plt

class Bond(object):
    def __init__(self, term, amount):
        self.term = term
        self.amount = amount

    def bond_return(self):
        if self.amount >= 3000:
            value = (1.03 ** self.term) * self.amount
            return (value - self.amount) / self.amount
        elif self.amount >= 1000:
            value = (1.01 ** self.term) * self.amount
            return (value - self.amount) / self.amount
        else:
            return False

    def f_value(self):
        return self.amount * self.bond_return() + self.amount

ListSt = []
ListLt = []
for i in range(99):
    ListSt.append(Bond(2+i, 1000).bond_return())
    ListLt.append(Bond(5+i, 3000).bond_return())

x, = plt.plot(ListSt)
y, = plt.plot(ListLt)
plt.legend([x, y], ['ST Bonds', 'LT Bonds'])
plt.show()





