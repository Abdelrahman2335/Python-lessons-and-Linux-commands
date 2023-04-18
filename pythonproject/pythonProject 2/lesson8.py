import os
#x = os.getcwdb()
#print(x)

#You can use this to change your location,But of course this is not the only use.

os.chdir('E:\\Body\\Photos')

#x = os.listdir()
#print(x)

#To read a photo we do the following process,you can't change w with r+ because there is no file to read, got it ?

#a = open('102408623_599332234324004_2694705339593408655_n.jpg',"rb")

a = open('Add a Moon in Photoshop 1.jpg',"rb")

#Here you are creating new file and b here means that this is image file.

new_photo = open("new_photo2.jpg","wb")

for line in a:
    new_photo.write(line)

print(os.listdir())

#import os
#os.chdir('C:\\Users\\dodom\\PycharmProjects\\pythonProject1')
#print(os.listdir())


