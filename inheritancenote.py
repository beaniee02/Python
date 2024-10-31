
class Animal:

    animal_type='mammals'
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def run(self):
        print(f'{self.name} is running')

    def eat(self):
        print(f'{self.name} is eating')

class Dog(Animal):
    def __init__(self, name, breed, height):
        # Animal.__init__(self, name, breed)
        super().__init__(name, breed)
        self.height = height
        
    def makesound(self):
        mk_sound=(f"{self.name} is barking")
        return mk_sound

class Goat(Animal):
    def __init__(self, name, breed, behavior):
        super().__init__(name, breed)
        self.behavior = behavior

    def makesound(self):
        return (f"{self.name} is barking")


dog1=Dog("stacey","rottweiler", "6.4")
goat1=Goat("eran iya osogbo","west african dwarf", 'stubborn')

print(dog1.animal_type)
print(goat1.animal_type)
print(goat1.eat())
print(goat1.makesound())
print(dog1.makesound())
print(dog1.height)
print(goat1.behavior)


class Vehicle:

    Vehicle_type = 'transport'   #class variable
    fuel_type = 'petrol'
    steering = 'one'
    brake = 'one'
    battery = 'one'
    def __init__(self, name, engine_type, tyre, speed): #instance variable
        self.name = name
        self.engine_type = engine_type
        self.tyre = tyre
        self.speed = speed

    def details(self):
        return (f'{self.name} has a {self.engine_type} engine and {self.tyre} tyres ')

    def park(self):
        return (f'{self.name} is parking.')

    def move(self):
        return f'{self.name} is moving at a speed of {self.speed}'
    
    def reverse(self):
        return f'{self.name} is trying to reverse'



class Car(Vehicle):
    def __init__(self, name, engine_type, tyre, speed, conditioning, bonnet): #instance variable
        super().__init__(name, engine_type, tyre, speed)
        self.conditioning = conditioning
        self.bonnet = bonnet

    def conditioner(self):
        conditioner_air = f'{self.name} has a {self.conditioning} conditioning system to keep you cool or warm you up'
        return conditioner_air
    
    def part(self):
        return f'{self.name} has a bonnet that houses a {self.bonnet} and other things that makes a car function'

class Maruwa(Vehicle):
    def __init__(self, name, engine_type, tyre, speed, cover): #instance variable
        super().__init__(name, engine_type, tyre, speed)
        self.cover = cover
    
    def canopy(self):
        return f'{self.name} uses {self.cover} to protect passengers'



car1 = Car('toyota', 'V6', 'four', '110km/hr', 'cold/warm', 'radiator')
maruwa1 = Maruwa('keke-napep', 'four-stroke', 'three', '90km/hr' 'tarpaulin')

print(car1.Vehicle_type)
print(maruwa1.Vehicle_type)
print(maruwa1.steering)
print(car1.steering)
print(car1.details())
print(maruwa1.details())
print(car1.conditioner())
print(maruwa1.canopy())