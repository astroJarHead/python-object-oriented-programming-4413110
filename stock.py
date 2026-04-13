# Challenge question #1: create a stock class

class Stock:
    # create the stock class: recall self references class itself
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    def get_description(self):
        # description = self.ticker+": "+self.company+" -- $"+str(self.price)
        # return description
        # school solution: one line! 
        return f"{self.ticker}: {self.company} -- ${self.price}"
        
