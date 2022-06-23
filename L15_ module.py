###Module is name of file to call

## To import module

#import mylibrary1 
#print(mylibrary1.mul(5,5))

#import mylibrary1 as ml  #use alias
#print(ml.mul(5,6))

#from mylibrary1 import *


#from mylibrary1 import mul #imports only selected functions
#print(mul(5,5))
#print(add(5,7))

from mylibrary1 import mul,add
print(mul(5,5))
print(add(5,5))
