# Animal class
class Animals:
    name = "" # Attribute for animal name

    # Constructor
    def __init__(self):
        print("An animal has been born.")
    
    # Eat method
    def Eat(self):
        print("Munch munch.")

    # Make Noise method
    def MakeNoise(self):
        print(f"Grrr says {self.name}.\n")

# Cat class, child class of the Animal class
class Cat(Animals):

    # Modified Constructor
    def __init__(self):
        print("A cat has been born.")
        return super().__init__()

    # MakeNoise method for Cat
    def MakeNoise(self):
        print(f"Meow says {self.name}.\n")

# Dog class, child class of the Animal class
class Dog(Animals):

    # Modified Constructor
    def __init__(self):
        print("A dog has been born.")
        return super().__init__()
    
    # MakeNoise method for Dog
    def MakeNoise(self):
        print(f"Bark says {self.name}.\n")
