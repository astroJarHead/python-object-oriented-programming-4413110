# Challenge question #1: create a stock class

class Stock:
    # create the stock class: recall self references class itself
    # with the __init__ method. These are instance attributes
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company
    # an instance method taking the class as first parameter
    # that is how the moethod accesses the attributes in the class
    def get_description(self):
        # description = self.ticker+": "+self.company+" -- $"+str(self.price)
        # return description
        # school solution: one line! 
        return f"{self.ticker}: {self.company} -- ${self.price}"
        
