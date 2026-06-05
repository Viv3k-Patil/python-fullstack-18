class Animal:
    def __init__(self, petname, age, breed, color):
        # define dog characteristics
        self.petname = petname
        self.age = age
        self.breed = breed
        self.color = color

    def walk(self):
        print(f"{self.petname} is walking")

    def drink(self):
        print(f"{self.petname} is drinking")

    def speak(self):
        print(f"{self.petname} is speaking")

class Dog(Animal):
    def __init__(self, petname, age, breed, color):
        super().__init__(petname, age, breed, color)

class Cat(Animal):
    def __init__(self, petname, age, breed, color):
        super().__init__(petname, age, breed, color)

a = Dog("Tommy", 6, "German Shephard", "Brown")

b = Dog("Moti", 5, "Street Dog", "Black")

c = Cat("Manimau", 2, "None", "white")
print("something")