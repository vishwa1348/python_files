#dictionary

#create a dictionary

##car={
##    "name":"ford",
##    "model":"mustang",
##    "year": 1964
##    }
##print(car)
##print(type(car))


#create a dictionary by dict()
##my_new_car=dict(name="ford",model="mustang",year=1964, color="white")
##print(my_new_car)
##print(type(my_new_car))

#access by key

# car={
#    "name":"ford",
#    "model":"mustang",
#    "year": 1964,
#    "year":2024,
#    "color":["red","white","black"]
#    }
# print(car)
#get by key name
# print(car.get("year"))
###key
##print(car.keys())
###values
##print(car.values())
##
###add new pair in dict
##car={
##    "name":"ford",
##    "model":"mustang",
##    "year": 1964,
##    }
##
##car["color"]="white"
##print(car)
##
###item()
##
##print(car.items())
##
###change the value of existing
##
##car["year"]=2020
##print(car)



#if condition in dict
##car={
##    "name":"ford",
##    "model":"mustang",
##    "year": 1964,
##    }
##
##if "color" in car:
##    print("yes, model is in car")
##else:
##    print("no, its not in the car")

# car={
#     "name":"ford",
#     "model":"mustang",
#     "year": 1964,
#     }

# car.update({"year":2024})
# print(car)


#remove a item in a dictionary
##car={
##    "name":"ford",
##    "model":"mustang",
##    "year": 1964,
##    }
##
##car.pop("year")
##print(car)

#popitem - last item remove

##car={
##    "name":"ford",
##    "model":"mustang",
##    "year": 1964,
##    }
##car.popitem()
##print(car)

##del car["name"]
##print(car)


##car.clear()
##print(car)

##del car
##print(car)


#for loop in dict

##car={
##    "name":"ford",
##    "model":"mustang",
##    "year": 1964,
##    }
##for i in car:
##    print(car[i])

##for i in car.keys():
##    print(i)

##for i in car.values():
##    print(i)
##

##for i in car.items():
##    print(i)


#copy

##car={
##    "name":"ford",
##    "model":"mustang",
##    "year": 1964,
##    }

##my_car=car.copy()
##print(my_car)

##my_car=dict(car)
##print(my_car)


#nested dictionary

##my_student_data={
##"student_1":{
##    "name":"vishwa kumaran",
##    "age":16
##    },
##"student_2":{
##    "name":"surya",
##    "age":16
##    },
##"student_3":{
##    "name":"varthu",
##    "age":16
##    }
##    }
##print(my_student_data)


student_1={
    "name":"vishwa kumaran",
     "age":16
    }
student_2={
    "name":"surya",
    "age":16
    }
student_3={
    "name":"varthu",
   "age":16
    }

my_students={
    "student_1":student_1,
    "student_2":student_2,
    "student_3":student_3  
    }

print(my_students)
