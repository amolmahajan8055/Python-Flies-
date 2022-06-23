##class,functions(method),object
class Usbcoach:
   a="chowk"
   b="duster"
#create a constructor
   def __init__(self):
        print("Hi,how are you")
 
#create a function(method)
   def teacher1(self):
        print("i am teacher1")

   def teacher2(self,a,b):
        print(a+b)

#create an object
stu1 = Usbcoach()
print(stu1.a)
print(stu1.b)
stu2 = Usbcoach()
print(stu2.b)
stu1.teacher1()
stu1.teacher2(2,3)


##Here,class is class,student is object and teacher is method(function)


