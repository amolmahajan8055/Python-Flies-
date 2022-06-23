## user defined functions

'''
def usb(name):
    print(name,', Welcome to usb')
    print('Great learning platform.')
usb('Amol')


def multiply(x,y):
    a=x*y
    print(a)

multiply(3,6)

def add(x,y,z):
    c=x+y+z
    return c
f=add(10,3,2)
print(f)

def add_sub(x,y,z):
    c=x+y+z
    d=x-y-z
    return c,d

f1,f2=add_sub(10,4,3)
print(f1,f2)

#Some built in functions
list1=[1,2,3]
t=(2,4,8)
print(len(t))
print(max(t))
print(sum(list1))
print(type(list1))
print(abs(-3))

#For more search, "in built functions">>>python.org

#######################################################################################################################
'''
##Practice
#1.define a function to subtract 2 numbers
def sub(x,y):
    a=x-y
    print(a)
sub(10,2)

######################################################################################################################

#2.define a function to divide 2 numbers
def div(x,y):
    b=x/y
    return b
f2=div(10,2)
print(f2)
#3.define a function to multiply 3 numbers
def mul(x,y,z):
    c=x*y*z
    return c
f3=mul(10,2,2)
print(f3)

########################################################################################################################

#4.define a function to add and sub two different numbers.


def add_sub(x,y):
    a=x+y
    b=x-y
    return a,b
f1,f2=add_sub(8,2)
print(f1,f2)

########################################################################################################################3

#5.fruits = ["apple", "banana", "cherry"] write a function name it 'code1',
#to return apple otherwise print not found,
#use code1 on nuts = ["mongo", "banana", "cherry","apple"]
fruits = ["apple", "banana", "cherry"]
nuts = ["mongo", "banana", "cherry"]
def code1(name):
    if 'apple' in name:
        print('apple is found')
    else:
        print('Not found')

code1(fruits)

code1(nuts)

#######################################################################################################################3


#6.fruits = ["apple", "banana", "cherry"] write a function to return
#apple and banana otherwise print not found. use this function on
fruits = ["apple", "cherry"]

def code2(name):
    if "apple" in name and "banana" in name:
        print('apple and banana found')
    elif "apple" in name:
        print('apple found')
    elif "banana" in name:
        print('banana found')
    else:
        print('not found')
    
code2(fruits)

greatfruits = ["pineapple","apple","greenbanana", "banana", "cherry"]
code2(greatfruits)

#######################################################################################################################

#7.print square of a number by user, define function for it
n=int(input('Enter a number: '))
def square(n):
    a=n*n
    return a
f=square(n)
print('The square of ',n,' is ',f)

#8. sort this list and define function for it
list1 = [589.36, 237.81, 230.87, 463.98, 453.42]
def sort_code(name):
    sorted_list=[]
    for i in range (len(name)):
        a=min(name)
        sorted_list.append(a)
        name.remove(a)
    list1.extend(sorted_list)
    print('Sorted list: ',list1)

sort_code(list1)

###################################################################################################################

#9.define a function which returns the number multiplied by 5

def multi(n):
    a=n*5
    return a
f2=multi(5)
print('Number multiplied by 5 = ',f2)

####################################################################################################################

#10.add new month to the list
month = ['Jan', 'Feb', 'Mar']
months = ['January', 'February', 'March']

def add_month(name):
    n=input('Enter a month: ')
    name.append(n)
    print('List after adding ',n,name)

add_month(month)

####################################################################################################################

#11.write a function to return square of list
list1=[2,3,6,8]
def square_list(name):
    list2=[]
    for i in name:
        a=i*i
        list2.append(a)
    print('Square list: ',list2)

square_list(list1)

####################################################################################################################
       
#12.define a function to return second largest from the list
a=[55,23,78,13,21,29,8]

def second_large(name):
    c=max(name)
    name.remove(c)
    b=max(name)
    print('The second largest number: ',b)

second_large(a)

###################################################################################################################

#13. print hello and user defined name

def hello(name):
    print('hello',name)

hello('abc')

#####################################################################################################################

#14.revese list and funtion for it
a=[55,23,78,13,21,29,8]

def reverse_list(name):
    rev=[]
    i=1
    x=len(name)
    while i <= x:
        p=name[x-i]
        rev.append(p)
        i=i+1
    print('Reverse list: \n',rev)
        
reverse_list(a)

####################################################################################################################        
   
#15.write a function to print table of 2

def table(n):
    for i in range(1,11):
        print(n*i)

table(2)
table(3)

####################################################################################################################
