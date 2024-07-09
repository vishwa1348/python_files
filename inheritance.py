#inheritance in python
#single inheritance
##class dad():
##    def phone(self):
##        print("dad mobile phone")
##
##class son(dad):
##    def laptop(self):
##        print("son laptop")
##
##obj1=son()
##obj1.laptop()
##obj1.phone()

#multiple inheritance

##class dad():
##    def phone():
##        print("dad mobile phone")
##
##class mom():
##    def sweet(self):
##        print("mom sweet")
##
##class son(dad,mom):
##    def laptop():
##        print("son laptop")
##
##obj=son()
##obj.laptop()
##obj.phone()
##obj.sweet()


#multilevel inheritance

##class grandpa():
##    def money():
##        print("money  ....")
##
##class dad(grandpa):
##    def phone():
##        print("dad mobile phone")
##
##class son(dad):
##    def laptop():
##        print("son laptop")
##
##obj=son()
#obj.laptop()
##
##obj2=dad()
##obj2.phone()
##obj2.money()
##obj2.money()
##obj2.phone()

#hierarchy inheritance

class dad():
    def money(self):
        print("money...")

class land():
    def land2(self):
        print("land...")
class son1(dad,land):
    pass
class son2(dad):
    pass
class son3(dad):
    pass
obj=son1()
obj.money()
obj2=son2()
obj2.money()
obj2.money()
