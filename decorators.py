#decorator function

def outer(func):
    def inner():
        print("thanks for entering")
        func()
        print("byee")
    return inner




@outer #decorators

def demo():
    print("welcome")

##demo=outer(demo) #decorator
demo()
