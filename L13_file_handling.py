### File handling in python

###Read files and close them


#f=open(r'C:\Users\Admin\Desktop\file1.txt')
#f=open('C:/Users/Admin/Desktop/file1.txt')
#f=open('C:\\Users\\Admin\Desktop\\file1.txt')


#print(f.read())     #read whole file
#print(f.read(2))    #read first two characters
#print(f.readline())  #read line by line
#print(f.readline())
#print(f.readline())
#print(f.readlines())
#f.close()


### No need to close file

#with open(r'C:\Users\Admin\Desktop\file1.txt') as f:
    #print(f.read())


### Combine open and read functions

#a1=open(r'C:\Users\Admin\Desktop\file1.txt').read()
#a1=open(r'C:\Users\Admin\Desktop\file1.txt').readlines()
#print(a1)

### Diffirent modes:
# 'r' = for reading,it is default mode,Error if dose not exist.'rb' = for binary file
# 'r+ = for reading and writing ,'r+b' for binary
# 'a' = open or creates file for appending i.e new data is add after last line.'ab' for binary file
# 'w' = open or creates for writing.overwrites existing content.creates if does not exist.
# 'w+' =open or creates for reading and writing,'w+b' for binary
# 'rt' = for reading text file.
# 'x' = creates new file for writing

### Write and Append
#a1=open(r'C:\Users\Admin\Desktop\file2.txt','a')
#a1.write('everything is clear and i am in')
#a1.close()

### lstrip and rstrip
#f1=open(r'C:\Users\Admin\Desktop\file2.txt','rt')
#a=(f1.read())
#print(a)
#b=a.lstrip('every')
#print(b)
#f1.close()

###split function
#f1=open(r'C:\Users\Admin\Desktop\file2.txt','rt')
#h=list(f1.read().split('i'))
#print(h)
#f1.close()

### Checking file pointer
## tell where is the pointer
#f=open(r'C:\Users\Admin\Desktop\file2.txt')
#print(f.read(8))
#print(f.tell())

### Read after second character
#f.seek(8)
#print(f.readline())
#print(f.tell())
#f.close()

####Practice
###1.Make a copy of file
#with open(r'C:\Users\Admin\Desktop\file2.txt') as f:
#    a=f.read()
#with open(r'C:\Users\Admin\Desktop\file3.txt','w') as f1:
#    f1.write(a)

###2.add your educational information in some already existing file

#with open(r'C:\Users\Admin\Desktop\file3.txt','a') as f:
#    f.write('\nMy educational qualification is : B.E. Mechanical')

###3.convert the given file in list and print the common data

#f= open(r'C:\Users\Admin\Desktop\hap.txt') 
#h1=list(f.read().split(', '))
#f.close()


#f1= open(r'C:\Users\Admin\Desktop\pri.txt')
#h2=list(f1.read().split(', '))
#f1.close()

#list1=[]
#for i in h1:
#    for j in h2:
#        if i==j :
#            list1.append(i)
#print(list1)

###4.store an hd image (use binary file) 
#with open(r'C:\Users\Admin\Desktop\img.jpg','rb') as f:
#    a=f.read()
#with open(r'C:\Users\Admin\Desktop\img1.jpg','wb')as f1:
#    f1.write(a)

###5.find number of lines in any text file

#f=open(r'C:\Users\Admin\Desktop\try.txt')
#count=0
#for i in f:
#    count+=1
#print('The no. of lines: ',count)
#f.close()


with open(r"C:\Users\Admin\Desktop\try.txt") as f:
   a=list(f.readlines())
   print(a)
   print("Number of lines are:",len(a))



