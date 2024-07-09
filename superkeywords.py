#super keywords


class a():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age:",self.age)

class b(a):
    def __init__(self,name,age):
        super().__init__(name,age)

    
obj=b("vishwa",16)
obj.name="kumaran"
obj.display()


#polymorphism


##def add(x,y,z=0):
##    return x+y+z
##print(add(1,2,4))


#overriding

##class animal():
##    def sound(self):
##        print("Animal makes sounds")
##
##class dog(animal):
##    def sound(self): #overriding - polymorphism
##        print("dogs barks")
##
##class bird(animal):
##    def sound(self):
##        print("birds sing")

##obj1=dog()
##obj1.sound()
##
##obj2=bird()
##obj2.sound()
##
##
##obj3=animal()
##obj3.sound()




#encapsulation

#private
##class company():
##    def __init__(self):
##        self.__name="google"
##
##    def display(self):
##        print(self.__name)
##
##
##
##google=company()
##google.display()


#encapsulation
from abc import ABC, abstractmethod

# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Create abstract method      
    @abstractmethod
    def printDetails(self):
        pass
  
    # Create concrete method
    def accelerate(self):
        print("Speed up ...")
  
    def break_applied(self):
        print("Car stopped")

# Create a child class
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Not having this feature")

# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Available")

# Create an instance of the Hatchback class
car1 = Hatchback("Maruti", "Alto", "2022")

# Call methods
car1.printDetails()
car1.accelerate()
car1.sunroof()






