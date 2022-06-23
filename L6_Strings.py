## Strings

#strings are a collection of characters
#they are written within '' & ""
#Strings are not mutable and case sensitive

# Creating a string
my_str1='This is my first string'
string="This is my second string"
print(my_str1) 
print(string)
print(type(string))

# Slicing of string
str1='This is my first string'
print('1.',str1)
print('2.',str1[:])

# print from index 1to 9
print('3.',str1[1:10])

# print till 'm' skipping value 1 element
print('4.',str1.index('m'))
print('5.',str1[0:9:1])

# print from index 0 to 13 skipping element 3
print('6.',str1[0:14:3])

# reverse the string
print('7.',str1[::-1])

# reverse indexing
print('8.',str1[-8:-1])
print('9.',str1[-8])

# assigning a value
a=(str1[2:10])
print('10',a)

# splitting string for the parameter passed
print('11.',str1.split('rst'))

# breaks the string into tuple passed
print('12.',str1.partition('rst'))

# replacing the string
print('13.',str1.replace('string','day'))

# return length
print('14.',len(str1))

# print count of character 't'
print('15.',str1.count('t'))

# convert to upper case
print('16.',str1.upper())

# convert to lower case
print('17.',str1.lower())

# return the index of element
print('18.',str1.index('first'))
print('19.',str1.find('first'))

# check last string
print('20.',str1.endswith('ing'))

str12="string"

# returns True, if alphanumeric string (example:abcde or 123)
print('21.',str12.isalnum())

# returns True if all the characters are alphabets (a to z)
print('22.',str12.isalpha())



############################################################################

#Practice
#1.create a string
str1='this is my first BIKE'
print('1.',str1)
print('2.',str1[:]) 



#1.print whole string
my_str = 'welcome to the lecture'
print(my_str)


#2.print  wloe
str3 = 'welcome to the lecture'
print('2.',str3[0:8:2])


#3.reverse the string
str3 = 'welcome to the lecture'
print('3.',str3[::-1])


#4.print 'the lecture'
print('4.',str3[11:22])


#5.print the length of string
str3 = 'welcome to the lecture'
print('5.',len(str3))


#6.print how many times 't' is repeated
str3 = 'welcome to the lecture'
print('6.',str3.count('t'))


#7.replace 'lecture' with 'session'
print('7.',str3.replace('lecture','session'))


#8.what is the index of 'o' ?
print('8.',str3.index('o'))
print('8.1.',str3.find('o'))


#9. convert string into upper case
str3 = 'welcome to the lecture'
print('9.',str3.upper())


#10. print 'welcome lecture'
str3 = 'welcome to the lecture'
print('10.',str3.split(' to the '))

#11.seperate each word by comma
print('11.',str3.split(' '))

#12.check if string is alphanumeric
print('12',str3.isalnum())

#13.check if string has last character 'e'
print('13',str3.endswith('e'))


