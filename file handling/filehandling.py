file=open("demo.txt","r")
# print(file)
file.write("helloo vishwa ")
print(file)
file.close()

# file.write("hiiiiiiiiiiiiiiiiiiiiiiiiii")
# print(file)
# file.close()

# file.write("hello vishwa")
# print(file)
# file.close()
# content=file.readline()
# print(content)
# file.close()


# import os

# # os.remove("demo.txt")

# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
# else:
#     print("the file does not exit ")

import os

os.rmdir("demo")