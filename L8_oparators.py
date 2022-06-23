## Operators

#Arithmatic operators
a=10
b=2

print('Addition',a+b)
print('Subtraction',a-b)
print('Multiplication',a*b)
print('Division',a/b)
print('Remainder',a%b)
print('Exponential',a**b)

#Assignment operators
print()
print("Assignment operators")
a=5
add,sub,mul,div,rem,expo=0,0,0,1,1,1

#add=add+a
add+=a
print('1.',add)
sub-=a
print('2.',sub)
mul*=a
print('3.',mul)
div/=a
print('4.',div)
rem%=a
print('5.',rem)
expo**=a
print('6.',expo)

#Comparison opearators
print()
print('Comparision operators')
a=5
b=10
#true if equal
print('1.',a==b)

#true not equal
print('2.',a!=b)

#true if a is greater than b
print('3.',a>b)

#true if b is greater than a
print('3.',b>a)

#true if a is greater than or equal to b
print('4.',a>=b)

#true if a is less than or equal to b
print('5.',a<=b)

#Logical opearators
print()
print('Logical operators')
a=5
b=0

#true if both are true
print('1.',a and b)

#true if either one is true
print('2.',a or b)

#returns opposite of value
print('3.',not a)
print('4.',not b)

#Identity operators
print()
print('Identity operators')
a=[1,2,3]
b=[2,3,4]

#true if a and b are equal
print('5.',a is b)

#True if a and b are not equal
print('6.',a is not b)

#true if 2 in a
print('7.', 2 in a)

#true if 2 in not b
print('8.',2 not in b)



###############################################################################


#1.take two int inputs from the user, print greatest among them

num1=int(input('chose 1 st no:'))
num2 = int(input("chose 2nd no: "))
if num1 >= num2:
    print(num1 ,'is greater ')
else:
   print(num2 ,'is greater ')

 #2.ask the user their Marks and grade accordingly
#Below 25 - F
#25 to 45 - E
#45 to 50 - D
#50 to 60 - C
#60 to 80 - B
#Above 80 - A

MARKS=int(input('marks?:'))
num=MARKS
if MARKS <25:
    print(num,' F ')
elif MARKS<45:
    print(num,' E ')
elif MARKS<50:
    print(num,' D ')
elif MARKS<60:
    print(num,' C ')
elif MARKS<80:
    print(num,' B ')
else: print (num,' A')


#3.take age as input from 3 users check who is oldest among them

a=int(input('a enter age1 '))
b=int(input('b enter age2 '))
c=int(input('c enter age3 '))

if a>b and a>c:  
 print(a,'is older')
elif a>b and c>a:
 print(c,'is older')
elif a<b and c<b:
 print(b,'is older')
else:print(c,'is older')



#4.take age as input from 3 users check who is youngest among them

a=int(input('a enter age1 '))
b=int(input('b enter age2 '))
c=int(input('c enter age3 '))

if a<b and a<c:  
 print(a,'is younger')
elif a<b and c<a:
 print(c,'is younger')
elif a>b and c>b:
 print(b,'is younger')
else:print(c,'is younger')


#5.take salary and no of service in a company as input from the user
#company decided to give bonus of 5% to employee, 
#if his/her year of service is more than 5 years
#print total amount and bonus amount.

salery=int(input('salery?:'))
exp=int(input('exp?:'))
if exp>5:
    print('new salery is ',salery*.05+salery,'bonus is',salery*.05)
else: print ('not applicable')



#6.Ask user for quantity of a product he purchased,
#A shop will give discount of 10% 
#if the cost of purchased quantity is more than 1000
#Suppose, one unit will cost 100.
#Judge and print discount for user and total cost.

user=int(input('total quantity ?:'))
if user>10:
    print('your discount is', user*100*0.1, ' :-so total cost is ', user*100-user*100*0.1)
else: print ('not applicable for discount')




#7.take Number of classes held and Number of classes attended and medical
#fitness as input from user, Allow him to attend exam if percentage 75. 

a=int(input('total no of classes held ?:'))
b=int(input('total no of classes attended ?:'))
c=int(input('medical fitness ?:'))
if ((b/a*100)+(c))/2 >=75:
    print('your are allowed to attend the exam')
else: print ('not allowed to sit for exam')



#8.take input as month from user(take only first six month)
#output should be no. of days in that month
a=input("Enter Month :-")
month1=['jan','mar','may']
month2=['apr','june']

if a in month1:
    print(a, "It has 31 Days")
elif a in month2:
    print(a, "It has 30 Days")
else :print(a, "It has 28 in a non Leap year and 29 Days in a Leap year")

##############################################################

b=input('Enter a month: ')


if b=='jan' or b=='mar' or b=='may':
        print('The no. of days in month ',b,'are 31')
elif b=='apr' or b=='jun' :
        print('The no. of days in month ',b,'are 30')
elif b=='feb':
        print('The no. of days in month ',b,'are 28')
else:
        print('You entered a wrong month.')



#9.take 10 inputs from the user, print greatest among them.

a=int(input('chose a no:'))
b=int(input('chose a no:'))
c=int(input('chose a no:'))
d=int(input('chose a no:'))
e=int(input('chose a no:'))
f=int(input('chose a no:'))
g=int(input('chose a no:'))
h=int(input('chose a no:'))
i=int(input('chose a no:'))
j=int(input('chose a no:'))

set1 = {a,b,c,d,e,f,g,h,i,j}
print('maximum value is ',max(set1))







