# Import the class ComboLock from CombinationalLock.py
from CombinationalLock import ComboLock  

# Test program for CombinationalLock.py
def main():   
    Combi = ComboLock(16,5,26)
    Combi.Reset()
    Combi.TurnRight(13)
    Combi.TurnLeft(1)
    Combi.TurnRight(20)
    Combi.Open()
    Combi.Reset()
    Combi.TurnRight(19)
    Combi.TurnLeft(7)
    Combi.TurnRight(4)
    Combi.Open()
    Combi.Reset()
    Combi.TurnRight(16)
    Combi.TurnLeft(11)
    Combi.TurnRight(21)
    Combi.Open()
main()