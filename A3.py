# -*- coding: utf-8 -*-
"""

@Author: Makenna Kidd

"""

# Answer to Question 1 
dict1 = {'e': 2,'j': 4,'a': 3,'t': 6,'q': 1}

### Place your code below this line ###

for keys, values in reversed(sorted(dict1.items())):
    print('key:',  keys, ";", 'value:', values)  

### Place your code above this line ###



# Answer to Question 2 

mylist = ['action', 'table', 'tennis', 'apple', 'trap']

### (WRITE YOUR DESCRIPTION OF THE dictionary setdefault() METHOD)

### 1. If a key is in the written dictionary, the setdefault() method 
### returns the value of the key. If the key is not in the dictionary, 
### the setdefault() method will insert a key with the default value 
### into the dictionary.

### 2. The syntax of the setdefault() method is that it takes two
### parameters: key - key to be searched  in the dictionary. 
### default_value(optional) - Key with a value default_value is 
### inserted into the dictionary if key isn't in the dictionary. 

### 3. The setdefault() method accepts a maximum of two parameters. 
### Key and default_value. The setdeault() method returns none if the 
### key is not in the dictionary and default_value is not provided. 
### Key is required, default_value is optional. 


### Place your code below this line ###

dictA = {}

for word in mylist:
    letter = word[0]
    if letter not in dictA:
        dictA[letter] = [word]
    else:
        dictA[letter].append(word)

dictA

### Place your code above this line ###

print('dictA:', dictA)



# Answer to Question 3 

A = set(range(2,21,2))
B = set(range(5,21,5))

### Place your code below this line ###

U = A.union(B)
I = A.intersection(B)
S = A.symmetric_difference(B)

### Place your code above this line ###

print('U:', U)
print('I:', I)
print('S:', S)



# Answer to Question 4 

def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

r = is_prime(1)
print( r)

print(type(r))

r = is_prime(5)
print(r)

r = is_prime(6)
print(r)

a = 'Prime' if is_prime(11) else 'Not prime'
print(a)



# Answer to Question 5 
lorem = 'ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip'
lorem_words = lorem.split(sep=' ')
print(lorem_words)

### (WRITE YOUR DESCRIPTION OF THE string split() METHOD)

### 1. The split() method splits a string into an array of substrings.
### The split() method then returns the new array. The split() method
### does not change the original string. 

### 2. The syntax of the split() method is that it takes two
### arguments: separator - which specifies what kind of separator . 
### to use for splitting the string. If this argument is not provided,
### the default value is any whitespace, meaning the string will split 
### whenever .split() encounters whitespace. The second argument 
### maxsplit, which specifies the maximum number of splits the .split() 
### method should perform. If this argument is not provided, the default 
### value is -1, meaning there is no limit on the number of splits, and 
### .split() should split the string on all the occurrences it encounters separator.

### 3. The split() method accepts two arguments. separator and maxsplit. 
###  Both of which are optional arguments. 

### (EXPLAIN IN YOUR OWN WORDS, HOW lorem_words GOT ITS VALUE)

### lorem_words got its value because the argument that was provided  
### was a whitespace string. Due to this, wherever there was whitespace
### is where the lorem string was separated which resulted in lorem_words
### printing the way that it did as:
### ['ut', 'enim', 'ad', 'minim', 'veniam', 'quis', 'nostrud', 'exercitation', 'ullamco', 'laboris', 'nisi', 'aliquip']

### Place your code below this line ###

word_len = {}

for word in sorted(lorem_words):
    length = len(word)
    word_len[word] = length

### Place your code above this line ###

print(word_len)



# Answer to Question 6 

def get_char_count_dict(txt):
    if type(txt) == str:
        dictionary = {}
        for char in txt.lower():
            if char != ' ':
                if char not in dictionary:
                    dictionary[char] = 0
                dictionary[char] += 1
        return dictionary
    return -1

#The examples given for Q. 6
s1 = 'The only impossible journey is the one you never begin!'
print(get_char_count_dict('little'))

print(get_char_count_dict('LiTtle'))

print(get_char_count_dict(127))

print(get_char_count_dict(s1))

print(get_char_count_dict(' '))



# Answer to Question 7 

### Place your code below this line ###

# A = {dictionary comprehension} something like this

A = {celsius: round((celsius * 9/5) + 32,1) for celsius in range(0,36,1)}

### Place your code above this line ###

print(A)



# Answer to Question 8 

dictionary = [{'name': 'John', 'age': 28, 'years': 2.5},
{'name': 'Lisa', 'age': 24, 'years': 3.1},
{'name': 'Ella', 'age': 31, 'years': 2.9}]
  
def sort_by_selected_key(dicts, keyname):
    result = sorted(dicts, key = lambda dicts: dicts[keyname])
    return(result)
    
print(sort_by_selected_key(dictionary, 'name'))
print(sort_by_selected_key(dictionary, 'age'))
print(sort_by_selected_key(dictionary, 'years'))



    
