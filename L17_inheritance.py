#inheritance
##Types of inheritance single,multi and multiple

#single inheritance(only grandfather in father)
class grandfather:
    def name1(self):
        print("vijay")

class father(grandfather):
    def name2(self):
        print("dinanath")
     
stu1 = father()
stu1.name1()
stu1.name2()

'''
#multi or multilevel inheritance(on calling son,father and grandfather
#are accessing.See their arguments)

class grandfather:
    def name1(self):
        print("vijay")

class father(grandfather):
    def name2(self):
        print("dinanath")
    
class son(father):
    def name3(self):
        print("chauhan") 
stu1=son()
stu1.name1()
stu1.name2()
stu1.name3()
'''
'''
#multiple inheritance(grandfather and father are individual class,in son)
class grandfather:
    def name1(self):
        print("vijay")

class father:
    def name2(self):
        print("dinanath")
    
class son(father,grandfather):
    def name3(self):
        print("chauhan")

stu1=son()
stu1.name1()
stu1.name2()
stu1.name3()
'''
