# import the value of tan and pi
from math import tan, pi

# Regular Polygon class
class RegularPolygon:

    # Constructor
    def __init__(self, N = 3, Side = 1, X = 0, Y = 0):
        self.N = N
        self.Side = Side
        self.X = X
        self.Y = Y
    
    # Accessors
    def GetN(self):
        return self.N
    def GetSide(self):
        return self.Side
    def GetX(self):
        return self.X
    def GetY(self):
        return self.Y

    # Mutators
    def SetN(self,N):
        self.N = N
    def SetSide(self, Side):
        self.Side = Side
    def SetX(self, X):
        self.X = X
    def SetY(self, Y):
        self.Y = Y

    # Calculates and returns the perimeter of the polygon
    def GetPerimeter(self):
        return self.N * self.Side

    # Calculates and returns the area of the polygon
    def GetArea(self):
        return self.N * (self.Side **2)/(4*tan(pi/self.N))