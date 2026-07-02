class Animal:

    def sound(self):
        print("Animal makes sound")

class dog(Animal):

    def bark(self):
        print("dog barks")

d = dog()

d.sound()
d.bark() 