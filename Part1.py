class Stbond(object):
    def __init__(self, term, amount, price):
        self.term = term
        self.amount = amount
        self.price = price

        if price <= 1000:
            print("Minimum price to invest is 1000!")
        if term <= 2:
            print("Minimum term for the sort term bond is 2 years")


    '''def stbond_return(self):
        self.price * self.term = x
        return x '''




