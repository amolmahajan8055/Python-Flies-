## Numeric Data

#1.0 Print function in python

print("This is my first day.")    #to print strings use double quotes

print('Hi,\n How is your day?')   #for new line use \n and use single quotes

print(1,2,3)                      #use "," to separate numbers

#2.0 Assign Variables

a=18
b=3
print('If a is',a,'and b is ',b,'\n Then a+b is:',a+b)

#3.0 Simple mathematical operations

print(a+b)
print(a-b)
print(a/b)

#4.0 Taking inputs from user (input function)

variable_1=input("Enter your name:")
variable_2=int(input("Enter your roll number:"))
variable_3=float(input("Enter your percentage:"))
print('Hi!',variable_1,'Welcome to USB','\nYour roll no. is:',variable_2,)
print('Your percentage is:',variable_3)

#5.0 Concatenate Data

var_1=input('Enter your name:')
var_2=int(input('Enter your roll number'))
print('Hi,' +var_1)
print('Your roll no. is' +str(var_2))

#6.0 Checking type of data

a=10
b=12.37
c=2+8j
d=7j
print(type(c))
print(type(a),type(b))
print(type(c),type(d))
#print(a+b)
#print(a+c)

#7.0 Implicit type of conversion

a=20   #Integer
b=-10
c=2.55  #Float
d=1.99
e=2+9j  #Complex
f=8j
print(a+c,b-f,a*b)

#8.0 Converting type of data

a=1   #Converting integer into float
b=float(a)
print(type(b),b)

c=2.8  #Converting float into integer
d=int(c)
print(type(d),d)

e=12   #Converting integer into string
f=str(e)
print(type(f),f)

####################################################################


#practice Q&A

var1=input('whats your name:')
var2=input('what is you house No:')
var3=input('what is your %')
print(' hi '+ var1,'\nwelcome to metaverse','\nyour house No is' ,var2,'\nyour % is',var3)
print(type(var1),type(var2),type(var3))

a=11  
b=-21
c=29.23
d=-73.44
e=5+3j   
f=-6+8j
print(type(a+c))
print(type(c-e))
print(type(b*f))
print(type(a+b))
print(a+c,c-e,b*f,a+b)









