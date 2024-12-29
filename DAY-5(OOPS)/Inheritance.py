class Student1:
    def printName(self):
        print("karan")
    
class Student2(Student1):
    def printage(self):
        print("18")

s2 = Student2()
s2.printName()
s2.printage()


# Multilevel Inheritance
print("\n\n MULTILevel INHERITANCE\n")

class Stu1:
    def printName(self):
        print("karan")
    
class Stu2(Stu1):
    def printage(self):
        print("18")
class Stu3(Stu2):
    def printUniversity(self):
        print("SR university")


s = Stu3()
s.printUniversity()
s.printName()
s.printage()

# Multiple Inheritance
print("\n\n MULTIPLE INHERITANCE\n")


class Stu1:
    def printName(self):
        print("karan")
    
class Stu2:
    def printage(self):
        print("18")
    def printName(self):
        print("this is student2 name method")
class Stu3(Stu1,Stu2):
    def printUniversity(self):
        print("SR university")


s = Stu3()
s.printUniversity()
s.printName()
s.printage()




# Hierarical inheritance

class Phone:
    def call(self):
        print("calling...")
    def message(self):
        print("message sent...")
    def game(self):
        print("playing game...")

class Vivo(Phone):
    def cam(self):
        print("50 MP")
    def storage(self):
        print("512 GB")
    def price(self):
        print("50000")
    def color(self):
        print("blue")
class Oppo(Phone):
    def color(self):
        print("black")
    def price(self):
        print("60000")
    def storage(self):
        print("1TB")

Vivo_mobile = Vivo()
Vivo_mobile.call()
Vivo_mobile.message()
Vivo_mobile.game()
Vivo_mobile.cam()
Vivo_mobile.storage()
Vivo_mobile.price()
Vivo_mobile.color()

Oppo_mobile = Oppo()
Oppo_mobile.call()
Oppo_mobile.message()
Oppo_mobile.color()
Oppo_mobile.price()
Oppo_mobile.storage()

