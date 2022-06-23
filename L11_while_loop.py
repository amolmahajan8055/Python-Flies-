##while loop
#Need to update the condition to end the loop

#Types of Nested loops
#1."for loop" within "for loop"
#2."for loop" within  "while loop"
#3. "while loop" within  "while loop"
'''
s=10
while s>=0:
    print(s)
    s-=1
print(s)

c=0

while c<=3:
    print(c)
    c=c+1
else:print('End')





##Practice

#1.using while loop check if number is less than 5

n=4
c=0
while c<3:
    if n<5:
        print('1. Number is less than 5.')
    c=c+1
    
#using  for loop
n=4
for i in range (n):
    if n<5:
        print('2. Number is less than 5')

###################################################################################################################

#2.take number from user print the addition of all the numbers 
#for eg- if input =3 output = 6(3+2+1)

n=int(input('Enter a number: '))
i=1
summ=0
while i<=n:
    summ+=i
    i+=1
print('1. The sum of first ',n,'terms is :',summ)


###OR

c=int(input('enter a no:'))
total=0
while c>=0:
    total+=c
    c-=1
else:print('the total is',total)


#using for loop
summ=0
for i in range (n+1):
    summ=summ+i

print('2. The sum of first ',n,' terms is : ',summ)

####################################################################################################################    

#3.print python using while loop
str1 = 'pythonfunctions'
i=0
while i<=5:
    print(str1[i],end='')
    i=i+1

#using for loop

str1 = 'pythonfunctions'    
for i in range (6):
    print(str1[i],end='')
print()

#####################################################################################################################

#4.print function from str1 using while loop
str1 = 'pythonfunctions' 
i=6
while i<=13:
    print(str1[i],end='')
    i=i+1
print()

#using for loop

str1 = 'pythonfunctions'    
for i in range (6,15):
    print(str1[i],end='')
print()

#####################################################################################################################

#5.print factorial of number given by user using while loop
n=int(input('Enter a nuber: '))
fact=1
i=1

while i<=n:
    fact=fact*i
    i=i+1

print('The factorial of ',n,' is: ',fact)

#using for loop

fact=1
for i in range (1,n+1):
    fact=fact*i
print('The factorial of ',n,' is',fact)

#####################################################################################################################

#6.print pythonfunctions but skip t and o using while loop
str1 = 'pythonfunctions'
i=0
while i<=14:
    if str1[i]=='t' or str1[i]=='o':
        print(end='')
    else:
        print(str1[i],end='')
    i=i+1
print()


str1 = 'pythonfunctions'
i=0
while i<=14:
    if str1[i]=='t' or str1[i]=='o':
        i=i+1
        continue
    else:
        print(str1[i],end='')
    i=i+1
print()


#using for loop
str1 = 'pythonfunctions'
for i in str1:
    if i=='t' or i=='o':
        continue
    else:
        print(i,end='')

print()
'''
#######################################################################################################################

#7.find the numbers less than 5 in  a=[1,2,4,5,6,7,8,9,10]
#and store in new list using while loop
a=[1,2,4,5,6,7,8,9,10]

i=0
less_than_5=[]
while i <len(a):
    if a[i]<5:
        less_than_5.append(a[i])
    i=i+1
print('The numbers less than 5 are ',less_than_5)

'''#using for loop
a=[1,2,4,5,6,7,8,9,10]
less_than_5=[]
for i in a:
    if i<5:
        less_than_5.append(i)
print('The numbers less than 5 are ',less_than_5)
'''

####################################################################################################################

#8.add 'well','done' to new list in above question using while loop
b=['well','done']
i=0
while i <len(b):
    less_than_5.append(b[i])
    i=i+1
print(less_than_5)

'''#using for loop

b=['well','done']
for i in b:
    less_than_5.append(i)
print(less_than_5)    
'''
######################################################################################################################
'''
a=[1,2,3,4,5,6,7,8,9]
b=[7,8,9,10,11,12,13,14,15]
#9.print common numbers of a and b using while loop
i=0
print('Common numbers: ')
while i<len(a):
    if a[i] in b:
        print(a[i],end='  ')
    i=i+1
print()
 
#using for loop
a=[1,2,3,4,5,6,7,8,9]
b=[7,8,9,10,11,12,13,14,15]
print('Common numbers: ')
for i in a:
    if i in b:
        print(i,end='  ')
print()

######################################################################################################################
    
#10.print uncommon numbers of a and b using for loop
a=[1,2,3,4,5,6,7,8,9]
b=[7,8,9,10,11,12,13,14,15]
i=0
j=0
print('Unommon numbers: ')
while i<len(a):
    if a[i] not in b:
        print(a[i],end='  ')
    i=i+1

while j<len(b):
    if b[j] not in a:
        print(b[j],end='  ')
    j=j+1
print()

#using for loop
a=[1,2,3,4,5,6,7,8,9]
b=[7,8,9,10,11,12,13,14,15]
print('Unommon numbers: ')

for i in a:
    if i not in b:
        print(i,end='  ')

for i in b:
    if i not in a:
        print(i,end='  ')

print()




#####################################################################################################################

#by using set functions
a=[1,2,3,4,5,6,7,8,9]
b=[7,8,9,10,11,12,13,14,15]

x=set(a)
y=set(b)

print('Set x = ',x)
print('Set y = ',y)

print('Common elements: \n',x&y)
print('Uncommon elements: \n',x^y)
'''

