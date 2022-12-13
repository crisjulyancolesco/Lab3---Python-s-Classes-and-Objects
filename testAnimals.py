# Import the Classes from Animals.py
from Animals import Animals
from Animals import Cat
from Animals import Dog

# Test Program for Animals.py
def main():

    Cat1 = Cat()
    Cat1.name = "Yang Yan"
    Cat1.Eat()
    Cat1.MakeNoise()

    Dog1 = Dog()
    Dog1.name = "Mo Fan"
    Dog1.Eat()
    Dog1.MakeNoise()

    Dog2 = Dog()
    Dog2.name = "Ling Ce"
    Dog2.Eat()
    Dog2.MakeNoise()

    Animal1 = Animals()
    Animal1.name = "Luo Zheng"
    Animal1.Eat()
    Animal1.MakeNoise()
    
main()