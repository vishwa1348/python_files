#exception handling

##print(dir(locals()["__builtins__"]))

##x=8
##result=x/0
##print(result)

x=[1,2,3]
try:
    print(x[4])
except Exception as e:
    print(f"error occured :{e}")
    
##else:
##    print("failed")
##finally:
## print("error")


try:
    raise NameError("hi hlo")
except NameError:
    print("error")
    raise
