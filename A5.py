# -*- coding: utf-8 -*-
"""

@Author: Makenna Kidd

"""

# Answer to Question 1 

import numpy as np

data1 = np.random.randn(5,3)
data1 , data1 * 100


# Answer to Question 2

import numpy as np

data2 = np.arange(10,21,2)
array1 = np.array(data2)
resultarray = np.reshape(array1, (2,3))
print(resultarray)


# Answer to Question 3

import numpy as np

data3 = np.arange(0,100,1)
array2 = np.array(data3)
resultarray2 = np.reshape(array2, (20,5))
print(resultarray2)



# Answer to Question 4

import numpy as np

contarray = np.random.random_sample(100)

array6 = np.reshape(contarray, (20,5))
array7 = np.copy(array6 * 100)

print(array6)
print(array7)



# Answer to Question 5

import pandas as pd
from pandas import Series

obj7 = pd.Series([0, 100, 200, 300, 400, 500], index = ['Column 0', 'Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5' ])
print(obj7)



# Answer to Question 6

import pandas as pd
from pandas import DataFrame

data10 = { 
    'state' : ['Ohio', 'Ohio', 'Arizona', 'Arizona'],
    'population' : [1.5, 1.7, 3.6, 4.1],
    'year' : [2000, 2001, 2000, 2002]
    }
frame10 = pd.DataFrame(data10)
print(frame10)