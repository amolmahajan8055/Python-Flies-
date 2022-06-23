## for loop

#simple for loop

list1=[1,2,3,'a','b','c']
for i in list1:
    print(i)

colors=['red','green','pink']
for color in colors:
    print(color,end=' ')

#add all elements in list

d=0
list2=[]
numbers=[1,2,3,4]
for i in numbers:
    d=d+i#d+=i
    list2.append(d)
print('\n',list2)

#using range function

print('By range function: ')

for i in range(10):
    print('1.',i)

for i in range (2,9):
    print('2.',i)

for i in range (0,20,1):  #for loop with range and skipping value
    print('3.',i)


# nested for loop
a=[1,2,3,4]
b=['a','b','c']

for i in a:
    for j in b:
        print(i,j,end='   ')
    print()



### Practice

#1.take year as input from user print the message
#if that year is leap year or not.

year=int(input('Enter a year: '))

if year%4==0:
    print('Leap year')
else:
    print('Not a leap year.')


#2.take unit as input from user and print the bill accordingly
#for first 100 units - no charge,than for each 100 units Rs 5 per unit flat.
#0-100 unit is Rs 0
#100-200 unit is Rs 5
#example:if user gives 102 units,
#than unit should be 5 and bill should Rs 10.

a=int(input('Enter units = '))
b=a//100


if a<101:
      print('No charge')


else:
    c=(a-100)*5*(b-1)
    print('Bill=Rs.',c)

###or

a=int(input('enter the units:'))
d=int(a/100)

if d<1:
    print('1.No charges')
else:
    print('1.Your 1unit = Rs',d*5,'and total bill is ',(a-100)*(d*5))


#3.print the elements in the list using for loop
c =['red','blue','white','orange']

for colour in c:
    print(colour)

#4.check if white is in the list,if yes print a message as "found"
#and at what index.(with loop and without loop)
c =['red','blue','white','orange']
if 'white' in c:
    print('Found at index',c.index('white'))
else:
    print('Not found.')

for i in c:
    if i=='white':
        print('Found at index',c.index('white'))

