#oops

#class and object

##class goa:
##    name="sangeetha"
##    regNo=0
##    def party(self):
##        print("partying.....")
##    def book(self):
##        print("book buy ... read")
##
##vishwa=goa( )
##kumaran=goa()
##
##vishwa.name="vishwa"
##vishwa.regNo=1
##kumaran.name="kumaran"
##kumaran.regNo=2
##vishwa.book()
##kumaran.party()
##vishwa.party()


class goa():
    book="read"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Book:",self.book)
        
obj1=goa("vishwa",15)
obj2=goa("kumaran",15)
obj1.display()  
obj2.display()




        
