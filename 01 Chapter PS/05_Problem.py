import os

#Specify the directory you want to list
directory_path = '/'
contents = os.listdir(directory_path)

#print each file
for items in contents:
    print(items)