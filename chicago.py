import pandas as pd
import os

__location__ = os.path.dirname(__file__)
file_path = os.path.join(__location__, 'chicago.tsv')
df = pd.read_csv(file_path)
# df = pandas.read_csv('/Users/josefiallos/Desktop/chicago.csv', sep='\t')
print(df.head()) #this is the head method to print the first 5 rows

print(type(df))  #this checks the panda data frame

#get the number of rows and columns
print(df.shape)

# get column names
print(df.columns)

#get the dtype of each columns
print(df.dtypes)

#get more information about the data
print(df.info())

Department_df = df['Department']

print(Department_df.head())

print(Department_df.tail())

# looking at department, job title and salary
subset = df[['title','Department','classification','exempt status','salary']]

print(subset.head())

print(subset.tail())

print(df.head())

#get first row
#python counts from 0
print(df.loc[0])

#get the 100th row
#python counts from 0
print(df.loc[99])

#get the last row correctly
number_of_rows = df.shape[0]

last_row_index = number_of_rows -1

print(df.loc[last_row_index])

print(df.tail(n=1))

subset_loc = df.loc[0]
subset_head = df.head(n=1)

print(type(subset_loc))

print(type(subset_head))

#select multiple number_of_rows
print(df.loc[[0,99,999]])

#get the 2nd row
print(df.iloc[1])

#get the 100th row
print(df.iloc[99])

df.iloc[0]

df.iloc[99]

df.iloc[[0,99,999]]

subset = df.loc[:,['Department', 'salary']]
print(subset.head())

department_size = df.groupby("Department").size()
print(department_size)
department_size.to_csv('department.csv')
