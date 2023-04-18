# Creating Class and Object in Python

class myBird:
    def __init__(self):
        print("myBird class constructor is executing...")
    def What_Type(self):
        print("I'm a Bird.")
    def Can_Swam(self):
        print("I can swam.")

# myPenguin class inheritong the attributes from the myBird class

class myPenguin(myBird):
    def __init__(self):
        super().__init__()
        print("myPenguin class constructor is executing...")
    def Who_Is_This(self):
        print("I'm Penguine.")
    def Can_Run(self):
        print("I can run faster.")

#Accessing the child class's attributes(Inheritance)

# pg1 = myPenguin()
# pg1.Who_Is_This()
# pg1.What_Type()
# pg1.Can_Swam()
# pg1.Can_Run()

class MyParrot:
    def Can_Fly(self):
        print("Parrot can fly easly:)")

    def Can_swam(self):
        print("But Parrot can't swam:(")
class myPenguin:
    def Can_Fly(self):
        print("Penguin can't fly:(")

    def Can_swam(self):
        print("But penguin can swam easly:)")

def flying_and_swam_bird_test(x_bird):
    x_bird.Can_Fly()
    x_bird.Can_swam()
bird_parrot = MyParrot()
bird_penguin = myPenguin()

flying_and_swam_bird_test(bird_parrot)
print()
flying_and_swam_bird_test(bird_penguin)
