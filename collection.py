#collections module

import collections
##print(dir(collections))
##
###counter - fn
##
##x=collections.Counter(["A","A","B","B","B","C","C"])
##print(x)
##y=collections.Counter([1,2,3,43,3,2,1,1,2,3,4,5,5,5,66,66,66])
##print(y)

#ordereddict

##d={}
##d["a"]=1
##d["b"]=2
##d["c"]=3
##for key , value in d.items():
##    print(key,value)
##
##d.pop("a")
##for key , value in d.items():
##    print(key,value)
##
##d["a"]=1
##for key , value in d.items():
##    print(key,value)


#namedtuple

student=collections.namedtuple("student",["name","age","DOB"])

x=student("vishwa",16,120421)
print(x)




