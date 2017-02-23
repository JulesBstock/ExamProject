class Stbond(object):
    def __init__(self, term, amount, interest):
        self.term = term
        self.amount = amount
        self.interest = interest

        if amount <= 1000:
            print("Minimum price to invest is 1000")
        if term <= 2:
            print("Minimum term for the sort term bond is 2 years")

    def stbond_return(self, amount, interest, term):
        self.amount = amount
        self.term = term
        self.interst = interest
        return amount * 0.01 * 100

print(Stbond.stbond_return(1000))




