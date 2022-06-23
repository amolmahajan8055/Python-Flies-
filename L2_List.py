 # List in Python

#-A list in Python is used to store the sequence of  various types of data.
#-Lists are mutable type it means we can modify its elements after it is created.
#-List is created by placing elements inside square brackets[] separated by comma.

#1.0 Initilising list

list_0=[]
print(list_0)

#2.0 Creating a list

list_1=[1,2,3,'Hello',4,5]
print(list_1)

list_2=list([5,6,'Hi',7])
print(list_2)
list_3=[0,1,2,3,4,5,6]

#3.0 Index function, (list[starting index : ending index : skipping value])

print(list_1[:])        # To print all elements of list
print(list_2[3])        # To print the value of element at 3rd index
print(list_3[0:4])      # To print the values from index 0 to 3
print(list_1[::-1])     # To print list in reverse order
print(list_1[-2:-5:2])
print(list_1[0:5:2])    # To print using skipping index 2
print(list_1[3][3])     # To print alphabet of string using index place

#4.0 append function (for adding one element at the end of the list

list_1=[1,2,3,'Hello',4,5]
list_2=list([5,6,'Hi',7])
list_3=[0,1,2,3,4,5,6]

list_2.append(10)       # To add element in the list
print(list_2)

list_2.append([11,12])  # To add two elements as one argument
print(list_2)

#5.0 extend function (for adding multiple elements to list)

list_2.extend([13])
print(list_2)

list_2.extend([14,15])  # To add two elements as two arguments
print(list_2)

#6.0 insert function

list_3.insert(3,'Good') # To add a element at a particular index
print(list_3)

#7.0 index function

print(list_2.index('Hi'))

#8.0 count function

print(list_1.count('Hello'))
print(list_1.count(3))

#9.0 len function

a=len(list_1)
print(a)
print(len(list_1))

#10.0 reverse function
list_3.reverse()
print(list_3)

#11.0 sort function

list4=[6,2,8,1,10,4,7,3,0,5,9]

#list4.sort()   #change the list by sort in ascending order
#print(sorted(list4))   #only print in ascending order
#print(list4)

list4.sort(reverse=True)   #sort in descending order
print(sorted(list4,reverse=True))
print(list4)

#12.0 copy function
list5=list4.copy()
print('list5 is',list5)

#13.0 pop function (use index)

a=(list4.pop(2))
print(a)
print(list4)

#14.0 remove function (for removing an element in the list use value)

list4.remove(7)
print(list4)

#15.0 del function (for deleting an element in list use index)

del (list4[2])
print(list4)

#16.0 clear function (for clearing the list)

list4.clear()
print(list4)

#17.0 replace an element in list

list5=[6,2,8,1,10,4,7,3,0,5,9]
list5[-2]='5 is replacing'
list5[3]=35
print(list5)

#####################################################################

##1.print welcome python1
#list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]
##2.table of 2 and 3
#list12 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
##3.add 'end' after python1 in list11
#new = [10,29,1,2,3,7,9,0,4,55]
##3.1 reverse list 'new'
##4.only print sorted list in ascending and descending order
##5.changing the list to sort descending order
##6.deleting 3 from list 'new' (use index)
##7.remove 29 from list 'new' (use values)
#8.pop 9 from list 'new' (uses index and returns the value)
##9.copy new list
##10. count '2' in list a
#a=[1,2,12,2,2,2,3,3,4,4,5,5,6,6,7,7,8,9,9,5,6,5,7,6,7,6,3,4,5]
##11.clear list 
##12.append "cup" in list11
##13.extend "tea" in list12
##14.add 32,41,55 in list 'new'
###15.add 22,32,42 as one index in list'new'
##16.replace '29' by 'done' in list 'new'



list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]
#1.print welcome python1

list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]
print(list11[0:5:4])

print(list11[0],list11[4])
a=list11[0]
b=list11[4]
print(a,b)

print(list11[-11:-6:4])

#list12 =(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

##2.table of 2 and 3

list12 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list12[1:20:2])

print(list12[2:20:3])


##3.add 'end' after python1 in list11
list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]

list11.insert(5,'end')
print(list11)


##3.1 reverse list 'new'
new = [10,29,1,2,3,7,9,0,4,55]

print(new[::-1])
new.reverse()
print(new)
print(new[-1:-10:-1])

##4.only print sorted list in ascending and descending order
list5= [10,29,1,2,3,7,9,0,4,55]

list5.sort()
print(list5)

print(sorted(list5))


print(sorted(list5,reverse=True))
print(list5)


##5.changing the list to sort descending order
list5= [10,29,1,2,3,7,9,0,4,55]
list5.sort(reverse=True)
print(list5)


##6.deleting 3 from list 'list5' (use index)
list5= [10,29,1,2,3,7,9,0,4,55]

list5.remove(3)
print(list5)

list5= [10,29,1,2,3,7,9,0,4,55]
del(list5[4])
print(list5)

list5= [10,29,1,2,3,7,9,0,4,55]
a=list5.pop(4)
print(list5)


##7.remove 29 from list 'list5' (use values)
list5= [10,29,1,2,3,7,9,0,4,55]
list5.remove(29)
print(list5)

list5= [10,29,1,2,3,7,9,0,4,55]
del(list5[1])
print(list5)

list5= [10,29,1,2,3,7,9,0,4,55]
a=list5.pop(1)
print(list5)


#8.pop 9 from list 'list5' (uses index and returns the value)
list5= [10,29,1,2,3,7,9,0,4,55]

a=list5.pop(6)
print(a)
print(list5)


##9.copy list5
list5= [10,29,1,2,3,7,9,0,4,55]
list6=list5.copy()
print('list 6 is',list6)



##10. count '2' in list a
a=[1,2,12,2,2,2,3,3,4,4,5,5,6,6,7,7,8,9,9,5,6,5,7,6,7,6,3,4,5]

print(a.count(2))

##11.clear list
list5= [10,29,1,2,3,7,9,0,4,55]

list5.clear()   
print(list5)

list5= [10,29,1,2,3,7,9,0,4,55]
del(list5[0:10])
print(list5)


##12.append "cup" in list11
list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]

list11.append('cup')  
print(list11)


##13.extend "tea" in list12
list12 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

list12.extend(['tea'])
print(list12)


##14.add 32,41,55 in list 'list5'
list5= [10,29,1,2,3,7,9,0,4,55]
list5.insert(10,'32,41,55')
print(list5)

list5= [10,29,1,2,3,7,9,0,4,55]
list5.extend([32,41,55])
print(list5)

list5= [10,29,1,2,3,7,9,0,4,55]
list5.append([32,41,55]) 
print(list5)


###15.add 22,32,42 as one index in list'list5'
list5= [10,29,1,2,3,7,9,0,4,55]
list5.append([32,41,55]) 
print(list5)

list5= [10,29,1,2,3,7,9,0,4,55]
list5.insert(10,'32,41,55')
print(list5)

##16.replace '29' by 'done' in list 'list5'
list5= [10,29,1,2,3,7,9,0,4,55]
list5[1]= ('done')
print(list5)















##############3
