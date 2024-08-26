class animal():
    def sound(self):
        print("Animal makes a sound.")

class Dog(animal):
    def sound(self):
        print("Dog barks.")

class bird(animal):
    def sound(self):
        return "Birds sing."
he=Dog()
he.sound()