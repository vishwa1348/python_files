# import pymongo
# import pymongo.mongo_client

# from pymongo import mongo_client

# client=mongo_client("mongodb+srv://vishwakumaranbalamurugan2024:dImdGH5ejQUNQn2q@cluster0.j6d5bzr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# mydb=client["python"]

# # print(client.list_database_names)
# print(client.list_database_names())



from pymongo import MongoClient

client = MongoClient("mongodb+srv://vishwakumaranbalamurugan2024:dImdGH5ejQUNQn2q@cluster0.j6d5bzr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


db=client.get_database("python")
collections=db.get_collection("sample")

print(client.list_database_names())

#inserting on data
document={
    "name":"vishwa",
    "age":16
}

res=collections.insert_one(document)

last_id=res.inserted_id

print(f"{last_id}")


#inserting many

students=[]

student1={
    "name":"kumaran",
    "age":16
}

student2={
    "name":"sangeetha",
    "age":16
}
student3={
    "name":"vardhu",
    "age":16
}

students.append(student1)
students.append(student2)
students.append(student3)

res=collections.insert_many(students)

#get information

res=collections.find_one()
print(res)

#getting all infor
res=collections.find()
for i in res:
    print(i)
