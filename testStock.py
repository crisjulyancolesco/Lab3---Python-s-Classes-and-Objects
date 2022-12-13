# Import the class Stock from Stock.py
from Stock import Stock

# Test program for Stock.py
def main():

    Stock1 = Stock("INTC", "Intel Corporation", 20.5, 20.35)
    print(f"""
    The Stock Symbol: {Stock1.GetSymbol()}
    Name: {Stock1.GetName()}
    Previous Price: {Stock1.GetPreviousPrice()}
    Current Price: {Stock1.GetCurrentPrice()}
    Price-Change Percentage:{Stock1.GetChangePercent()}""")

main()