# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description  # attribute of the Item class and any subclasses
        self.value = value  # attribute of the Item class and any subclasses

    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Extend the Items class
# Gold class will be a child or subclass of the superclass Item


class Lunarglasses(Item):
    # __init__ is the contructor method
    def __init__(self, Zoom):
        self.Zoom = Zoom  # attribute of the lunarglass class
        super().__init__(name="Lunarglasses",
                         description="the glases with {} zoom for night vision. Night Vision devices".format(
                             self.Zoom),
                         value=self.Zoom)


class Transport:
    def __init__(self):
        self.name = 'walk'
        self.description = 'walking to other districts'

    def RailorHovercraft(self, speed):
        if(speed <= 500 and speed >= 20):
            self.name = "Higest speed"
            self.description = "you are travelling at speed multiple by 2 times"
            print("=== {} at speed {} km/h".format(
                 self.description, speed))

        elif(speed > 500):
            self.name = "Speed"
            self.description = "you are travelling at speed multiple by 3 times"
            print("=== {} at speed {} km/h".format(
                self.description, speed))
        else:
            self.name = "Speed"
            self.description = "you are travelling at speed less than 20KM/hr"
            print("=== {} at speed {} km/h".format(
                self.description, speed))

    def __str__(self):
        return "{}\n=====\n{}\n speed: ".format(self.name, self.description)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Titan(Weapon):
    def __init__(self):
        super().__init__(name=" Titan",
                         description="You have the Titan weapon.use it to kill the enemy and survive!",
                         value=0,
                         damage=15)


class Knowhere(Weapon):
    def __init__(self):
        super().__init__(name="Knowhere",
                         description="Use knowhere and fight against the emeny on the planet",
                         value=10,
                         damage=10)


class Vormir(Weapon):
    def __init__(self):
        super().__init__(name="Vormir",
                         description="Use vomir and fight against the emeny on the planet",
                         value=0,
                         damage=25)


class Zen(Weapon):
    def __init__(self):
        super().__init__(name="Zen",
                         description="Use Zen and fight against the emeny on the planet",
                         value=1,
                         damage=20)


class Nidavellir(Weapon):
    def __init__(self):
        super().__init__(name="Nidavellir",
                         description="Use Nidavellir and fight against the emeny on the planet",
                         value=2,
                         damage=25)

class Muller(Weapon):
    def __init__(self):
        super().__init__(name="Muller",
                         description="Use Muller and fight against the emeny on the planet",
                         value=2,
                         damage=25)


class Antidote(Item):
    def __init__(self, name, description, value, amt, health):
        self.amt = amt
        self.health = health
        super().__init__(name, description, value)


class AntidoteLeaves(Antidote):
    def __init__(self):
        super().__init__(name='AntidoteLeaves',
                         description='A small potion', value=5, amt=5, health=30)
