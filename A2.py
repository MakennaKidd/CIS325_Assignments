# -*- coding: utf-8 -*-
"""

@Author: Makenna Kidd

"""

# Answer to Question 1 

for i in list(range(2,28,2)):
    print('Generated number: ', i)


# Answer to Question 2

for i in list(range(3,0,-1)):
    for j in list(range(1001,1006,1)):
        print(i,';',j)


# Answer to Question 3 

input1 = int(input('Enter an integer number: '))

### Place your code below this line ###

if input1 < 0:
    print('Input1 is negative')
elif input1 == 0:
    print('Input1 is zero')
elif 0 < input1 <= 20:
    print('Input1 is positive but less than or equal to 20')
else:
    print('Input1 is greater than 20')

### Place your code above this line ###


# Answer to Question 4 

j = 0 
sum11 = 0

while j < 10:
    ### Place your code below this line ###
    
    print(f'j: {j} sum 11: {sum11}')
    
    if j == 9:
        break 
    
    j += 1 
    sum11 = j * 11 + sum11
    
    ### Place your code above this line ###

print('')
print('Total sum11 is: ', sum11)


# Answer to Question 5 

historical = 3, 5, 1, 9, 0, 3, 9, 2, 4, 7
predictiona = 1, 5, 4, 1, 7, 7, 1, 0, 3, 9
predictionb = 6, 0, 4, 3, 4, 4, 8, 4, 3, 7

print('')
print('historical: ', historical)
print('predictiona: ', predictiona)
print('predictionb: ', predictionb)
print('')
 
### Place your code below this line ###

topresults = zip(historical, predictiona, predictionb)

for  h, a, b in topresults:
    print('historical: ',  h, 'prediction a: ', a, 'prediction b: ', b)

### Place your code above this line ###


# Answer to Question 6 

### Place your code below this line ###

btcdec1 = [11234, 12475]
btcdec1.append(14560)

btcdec2 = [] 
btcdec2.append(15630)
btcdec2.append(12475)
btcdec2.append(14972)

btcdec1.extend(btcdec2)

btcdec2.remove(15630)
btcdec2.remove(12475)
btcdec2.remove(14972)

btcdec1.sort()

### Place your code above this line ###

print(btcdec1)


# Answer to Question 7 

list1 = [-4, 2, 7, -6, 3, -5, 8, 10, 4, -10]
list2 = [1, 7, 8, -10, 2, 6, -1, 10, -3, -8]

cnt = 0

lookup = {}

for item in list1:
### Place your code below this line ###

    lookup[item] = 1
    
for item in list2:
    if item in lookup and lookup[item] > 0:
        cnt += 1    
        
### Place your code above this line ###
    
print('Number of common items between list1 and list2 is: ', cnt)


# Answer to Question 8 

growth_rates = [1.03, 0.9, 1.36, 1.23, 1.08, 1.12, 1.55, 1.06, 1.05, 0.92]

### Place your code below this line ###

mult = 1

for i in growth_rates:
    mult = (mult) * i
    
n = len(growth_rates)

geo_mean = round((mult) ** (1/n), 2)

### Place your code above this line ###

print('Compounded annual growth rate is: ', geo_mean)
