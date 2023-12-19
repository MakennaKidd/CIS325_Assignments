"""

@Author: Makenna Kidd

"""

# Answer to Question 1 

gyear = 1994
myear = 1997
ranfloatnum = 26.5

results1 = gyear + myear + ranfloatnum

print(results1)
print(type(results1))


# Answer to Question 2

string1 = '''This is a longer string
that spans multiple lines'''

s = string1.count('s')

print(string1.count('s'))


# Answer to Question 3

import math

var1 = math.pi

print(round(var1, 3))


# Answer to Question 4

var1 = int(input('Enter a var1 number: '))
var2 = int(input('Enter a var2 number: '))

### Place your code below this line ###

var3 = var1 * var2

### Place your code above this line ###

print('')
print('The result of multiplying var1 and var2 is: ', var3)


# Answer to Question 5

numerator1 = '32000'
denominator1 = '1000'

newnumval = float(numerator1)
newdenval = float(denominator1)

answer = newnumval / newdenval

print(answer)


# Answer to Question 6

year = 1991
author = 'Guido van Rossum'

### Place your code below this line ###

text1 = 'Python is a general-purpose programming language released in ' + str(year) + ' by ' + author

### Place your code above this line ###

print(text1)


# Answer to Question 7

sunny = True
warm = False

print('Is it True or False that I should go out for ice cream?:', (sunny and warm))

# What results do you expect from the print statement,
# and why Python provided such result?
# 
# If both instances are true, then it will print a True else it will print False.
# because it has an and statement with both variables.
# Since Sunny is true and Warm is False, it will print False.


# Answer to Question 8

# Add correct import statement
from datetime import datetime

dt = datetime(2021, 9, 6, 18, 51, 17)

### Place your code below this line ###

#timedelta object
from datetime import timedelta

dt2 = dt - timedelta(28)

dt2_str = dt2.strftime('%m/%d/%Y')

### Place your code above this line ###

print('dt2_str date is:', dt2_str)
