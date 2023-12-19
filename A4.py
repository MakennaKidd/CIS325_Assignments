# -*- coding: utf-8 -*-
"""

@Author: Makenna Kidd

"""

# Answer to Question 1

import random

### (WRITE YOUR DESCRIPTION OF THE randint() FUNCTION FROM THE random PACKAGE)

# 1. What does randint() do?
#
# The randit() function is used to generate a random integer between two specified
# limits that are inclusive.


# 2. What is the syntax of randint()?
#
# The syntax for randint is: random.randint(start-int, stop-int)

# 3. What are the arguments and what do they do? Are they required or optional?
#
# randint() takes two arguments. A start, and a stop. Both of which are required. 
# The start is for an integer which specifies at which position to start. 
# The stop is for an integer which specifies at which position to stop. 

### Place your code below this line ###

randomnumlist = []

def lottery(n = 6):
    for i in range(1, n+1):
        n = random.randint(1,40)
        randomnumlist.append(n)
        yield n
    
# Tests to check for quality assurance
g = lottery(2)
print(type(g))

x = next(g)
print(x)

x = next(g)
print(x)

a = list(lottery())
print(a)

b = tuple(lottery(n = 10))
print(b)

for i in lottery(4):
    print('Random number:', i)

### Place your code above this line ###

### (DIFFERENCE BETWEEN yield AND return)
#
# The yield and return statements are both used to send values back from a function, 
# but they have different behaviors. 
#
# return: is used to terminate the execution of a function and send a single value back 
# to the caller. Once a function returns, it cannot be called again. 
#
# yield: is used to pause the execution of a function and send a value back to the caller.
# The function can then be resumed later, and it will continue execution from where it 
# left off. A function can yield multiple values.  



# Answer to Question 2 

import math

def valueErrors(x)
        return float(x)
        
valueErrors('Hello World')
valueErrors(math.sqrt(-1))
valueErrors(random.randint(-5,-20))
valueErrors('N a N')
valueErrors(chr(5))



# Answer to Question 3

import math

def typeErrors(x):
    return float(x)

typeErrors(len(x))
typeErrors(None)
typeErrors(complex(1, 2))
typeErrors([1,2,3])
typeErrors({'age','year','month'})



# Answer to Question 4 

def break_modules(x, y):
    try:
        result = x/y
        print(result)
    except ZeroDivisionError:
        print("All numbers must be greater than zero")
    except TypeError:
        print("Unknown error, please check your numbers.")

# Tests to check for quality assurance
break_modules(5, 2) #Normal function which will print 2.5
break_modules(7, 0) #Dividing by zero which will print the zero division error
break_modules(7, 'ten') #Dividing by incorrect type which will print the type error. 



# Answer to Question 5 

class myfirstclass:
    def __init__(self, num):
        self.num = num

    def methoda(self):
        print(self.num ** 2)


    def methodb(self):
        print(self.num ** 3)


# Tests to check for quality assurance
myobj = myfirstclass(4)
myobj.methoda()
myobj.methodb()



# Answer to Question 6 

class parentclass:
    
    ### Place your code below this line ###
    
    def __init__(self, number):
        self.number = number

        
    def methoda(self):
        print(self.number ** 2)
    
    ### Place your code above this line ###
        
class childclass(parentclass):
    
    ### Place your code below this line ###
    
    def methodb(self):
        print(self.number **3)
         
    def methodc(self):
        print(self.number ** 4)
            
    ### Place your code above this line ###
        
    
myobj1 = childclass(10)
myobj1.methoda()
myobj1.methodb()
myobj1.methodc()