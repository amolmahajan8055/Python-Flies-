## Conditional statements

num=3
if num > 0:
    print(num,' is positive')

num=-1
if num > 0 :
    print(num,' is positive')

## Program checks if the numbers is positive or negative
# and displays an appropreate message

num=5
if num >= 0 :
    print(num,' is positive')

else:
    print(num,' is negative')

## check if number is positive, negative or zero

#num=2
#num=0
num=-3

if num > 0:
    print(num,' is positive')
elif num==0:
    print(num,' is zero')
else:
    print(num,' is negative')

# The symbol "%" in python is called the 'Modulo'. It returns the remainder
#2%2=0
#3%2=1

## Nested if else

n=5

if n >= 0:
    if n==0:
        print('number is zero')
    else:
        print('number is positive')
else:
    print('number is negative')
    


##########################################################################


#1.check if number is positive, if yes then add 5 to it and print the output

num=3
if num > 0:
   print(num,' is positive ')
print(num+5)


#2.check if number is negative number if yes multiply it by 10 print the output

num=-3
if num < 0:
   print(num,' is negitive ')
print(num*10)


#3.if number is positive add 10 to that number if it is negative multiply by 10
#and print the output accordingly

#num=3
num=-3

if num > 0:
   print(num,' is positive')
   print(num+5)
else:
    print(num*10)


#4.If number is multiple of 2 print a message
num=8
if num%2 == 0:
        print ('no is multiple')


#5.now check if number is multiple of 3
#if yes add 100 to the number 
#if not then return its square

num=10
if num%3 == 0:
        print ('no is multiple')
        print(num+100)
else:
       print(num*num)


#6.write a program such that if input is positive number 
# output is same positive number, if input is negative number still output
# is positive number Take input from user

var1=input('whats your name:')
var2 = float(input("Enter a number: "))
print(' hi ',var1,'\nwelcome to metaverse','\nyour  No is ',var2)
num=var2
if num >= 0:
    print(num)
else:
   print('output is',-num)



#7.take a sides of quadrilateral from user and check if it is a square or not
   
var1 = float(input("Enter the side of quad: "))
var2 = float(input("Enter the side of quad: "))
var3 = float(input("Enter the side of quad: "))
var4 = float(input("Enter the side of quad: "))
if var1==var2==var3==var4:
    print ('quad is square')
else:
   print('quad is not a square')


#8.in the above question find area if it is a square
var1 = float(input("Enter the side of quad: "))
var2 = float(input("Enter the side of quad: "))
var3 = float(input("Enter the side of quad: "))
var4 = float(input("Enter the side of quad: "))
if var1==var2==var3==var4:
    print ('quad is square')
area=var1*var1
print('area is ',area, 'mm2')


#9.Take positive Radius of circle and find its area. Message if negative
var1 = float(input("enter radius: "))
if var1>0:
    area=3.14*var1*var1
    print('area of circleis', area)
else:
    print(var1,' is negitive ')


 



    

