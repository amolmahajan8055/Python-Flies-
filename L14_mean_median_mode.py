### Mean, Median and Mode

##Mean is average value.

#1. Find mean of given numbers.
#a. 9,7,11,13,2,4,5,5  \\7
a=[9,7,11,13,2,4,5,5]
 
mean_a=sum(a)/len(a)

print('The mean of a is ',mean_a)

#b) 16,18,19,21,23,23,27,29,29,35  \\24

b=[16,18,19,21,23,23,27,29,29,35]

mean_b=sum(b)/len(b)

print('The mean of b is ',mean_b)

#c) 2.2,10.2,14.7,5.9,4.9,11.1,10.5  \\8.5

c=[2.2,10.2,14.7,5.9,4.9,11.1,10.5]

mean_c=sum(c)/len(c)

print('The mean of c is ',mean_c)

## Median is the central value when data arranged in ascending order

#1. Find median of given numbers.
#d) 12,17,3,14,5,8,7,15//10


d=[12,17,3,14,5,8,7,15]
d.sort()

l=len(d)
x=l//2

if l%2==0:
    median=(d[x]+d[((x)-1)])/2
else:
    median=(d[x])

print(median)

# MODE

#a) 12,8,4,8,1,8,9,11,9,10,12,8//8

a = [12,8,4,8,1,8,9,11,9,10,12,8]

b = list(set(a))
list1 = []
for i in b:
    n = a.count(i)
    list1.append(n)
x = list1.index(max(list1))

mode = b[x] 

if max(list1) == 1:
    print('No mode')
else:
    print('Mode: ',mode)

####OR

list3 = [12,8,4,8,1,8,9,11,9,10,12,8]
count = 0
x = 0
for i in list3 :
    a = list3.count(i)
    if count <= a:
        count = a
        x = i
if count == 1:
    print("No mode")
else:
    print("count of mode = ",count,"\nmode = ",x)
  

#b) 15,22,17,19,22,17,29,24,17,15//17
#c) 0,3,2,1,3,5,4,3,42,1,2,0//3
#d) 1,7,2,4,5,9,8,3//no mode


#To CALCULATE THe STANDARD DEVIATION

b = 0
list4 = [1,2,3,4]
mean = sum(list4)/len(list4)
for i in list4:
    x = (((i-mean)**2)/len(list4))
    b = b+x

print('Standard Deviation = ',b**0.5)
