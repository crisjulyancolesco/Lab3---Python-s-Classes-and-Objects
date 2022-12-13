# Stock class
class Stock:

    # Constructor
    def __init__(self, Symbol, Name, PreviousPrice, CurrentPrice):
        self.Symbol = Symbol
        self.Name = Name
        self.PreviousPrice = PreviousPrice
        self.CurrentPrice = CurrentPrice
        
    # Returns the Stock's symbol
    def GetSymbol(self):
        return self.Symbol

    # Returns the Stock's name
    def GetName(self):
        return self.Name

    # Gets the previous price
    def GetPreviousPrice(self):
        return self.PreviousPrice
    
    # Gets the current price
    def GetCurrentPrice(self):
        return self.CurrentPrice
    
    # Sets the previous price
    def SetPreviousPrice(self, PreviousPrice):
        self.PreviousPrice = PreviousPrice
    
    # Sets the previous price
    def SetPreviousPrice(self, CurrentPrice):
        self.PreviousPrice = CurrentPrice

    # Calculates the percentage change of the stock's price
    def GetChangePercent(self):
        return ((self.CurrentPrice - self.PreviousPrice)/self.PreviousPrice)* 100
