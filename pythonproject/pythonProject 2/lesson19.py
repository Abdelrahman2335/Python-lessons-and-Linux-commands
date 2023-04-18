# Multiple Inheritance:

class Base1:
    def x(self):
        print("X is executing...")

class Base2:
    def y(self):
        print("Y is executing...")
class Base3:
    def z(self):
        print("Z is executing...")
class Multi_Derived(Base1, Base2, Base3):
    def a(self):
        print("A is executing...")

m1 = Multi_Derived()

m1.x()
m1.y()
m1.z()
m1.a()