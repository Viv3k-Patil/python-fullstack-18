class dog:

    def sound(self):
        print("dog barks")

class cat:

    def sound(self):
        print("cat meow")

for animal in [dog(), cat()]:
    animal.sound()