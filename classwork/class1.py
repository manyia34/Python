""" write a python program to print the content of a directory using the os module . Search 
online for the function which does not """

# os.listdir() return a list of files and floders present in the current directory
import os
# files = os.listdir()
# print(files)

# # using looping
# items_list = []
# for items in os.listdir():
#     items_list.append(items)
# for i in items_list:
#     print(i)


# # getcwd() is a function which is used to get the current working directory
# print(os.getcwd())


# # os.path.exists() checks whether a given path exists, returns True/False
# path_file = os.path.exists(r"C:\Users\sm201\Desktop\Python\manyia")
# if path_file:
#     print("True")
# else:
#     print("False")
    
# # rename the name of the folder or the file
# os.rename("folder","classwork")

# use a function to check whether the this is a file
# print(os.path.isfile("class1.py"))

# use a function to check whether the this is a folder
# print(os.path.isdir("classwork"))

# Write a method to remove the file 
# os.remove("rough.py")

# write a method to remove the directory
os.rmdir("rough")