from Geometry import RegularPolygon

def main():
    Polygon1 = RegularPolygon()
    print(f"The Perimeter of Polygon1 is {Polygon1.GetPerimeter()}")
    print(f"The Area of Polygon1 is {Polygon1.GetArea()}")

    Polygon2 = RegularPolygon(6,4)
    print(f"The Perimeter of Polygon2 is {Polygon2.GetPerimeter()}")
    print(f"The Area of Polygon2 is {Polygon2.GetArea()}")

    Polygon3 = RegularPolygon(10,4,5.6,7.8)
    print(f"The Perimeter of Polygon3 is {Polygon3.GetPerimeter()}")
    print(f"The Area of Polygon3 is {Polygon3.GetArea()}")

main()