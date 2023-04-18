import os
# print(os.getcwd())
#To get the cwd like this '' \\ we use this function: why I need to use this? you will need it in the next function :)
print(os.getcwdb())

os.chdir('/home/kali/pythonproject')

# os.chdir('/home/kali/C_file')

#To read what's inside pythonproject folder:
print(os.listdir())

#To know where is your location:
#print(os.getcwdb())

#To add FOLDER his name is "Hello there" (in pythonproject):
#os.mkdir("Hello there")

#To rename "Hello there"
#os.rename("Hello there","I renamed this folder")

#We use this to delete FILES:
#os.remove("Hello there")

#We use this to delete FOLDERS:
#os.rmdir("I renamed this folder")

#Her I'm telling python that I'm working her:

#os.chdir("C:\\Users\\dodom\\PycharmProjects\\pythonProject1")





