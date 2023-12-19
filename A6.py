# -*- coding: utf-8 -*-
"""

@Author: Makenna Kidd

"""

# Answer to Question 1 

import pandas as pd

df = pd.read_csv(r'C:\Users\Kenna\Desktop\School\CIS 325\Assignments\loan-data-v1.csv')

df.to_json(r'C:\Users\Kenna\Desktop\School\CIS 325\Assignments\loan-data-v1.json')
df.to_excel(r'C:\Users\Kenna\Desktop\School\CIS 325\Assignments\loan-data-v1.xlsx')
df.to_html(r'C:\Users\Kenna\Desktop\School\CIS 325\Assignments\loan-data-v1.html')


# Answer to Question 2

import pandas as pd

df2 = pd.read_excel(r'C:\Users\Kenna\Desktop\School\CIS 325\Assignments\loan-data-v1.xlsx')

subset_df2 = df2[['Name', 'Annual Income', 'Loan Type', 'Loan Amount']]

html_output = subset_df2.to_html()
with open( 'results2.html', 'w') as f:
    f.write(html_output)


# Answer to Question 3

import pandas as pd

df3 = pd.read_excel(r'C:\Users\Kenna\Desktop\School\CIS 325\Assignments\loan-data-v1.xlsx')

state_selection = df3[df3['State'] == 'UT']
subset_df3 = state_selection[['Age', 'Days Delinquent', 'Loan Amount']]

json_output = subset_df3.to_json(orient = 'records')
with open( 'results3.json', 'w') as f:
    f.write(json_output)


# Answer to Question 4 

import numpy as np
import pandas as pd

random_sample = np.random.randn(100001)

random_series = pd.Series(random_sample)

random_series.to_csv(r'C:\Users\Kenna\Desktop\School\CIS 325\Assignments\results4.csv')

