import pandas as pd

# Create the first DataFrame
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Anu', 'Ravi', 'Sita', 'Kiran'],
    'Department': ['CSE', 'ECE', 'CSE', 'IT']
})

# Create the second DataFrame
df2 = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'Marks': [85, 90, 78, 88],
    'City': ['Vizag', 'Hyderabad', 'Chennai', 'Delhi']
})

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

# 1. Merge using a common column
print("\nInner Merge:")
print(pd.merge(df1, df2, on='ID', how='inner'))

# 2. Left merge
print("\nLeft Merge:")
print(pd.merge(df1, df2, on='ID', how='left'))

# 3. Outer merge
print("\nOuter Merge:")
print(pd.merge(df1, df2, on='ID', how='outer'))

# 4. Concatenate DataFrames row-wise
print("\nRow-wise Concatenation:")
print(pd.concat([df1, df1], axis=0, ignore_index=True))

# 5. Concatenate DataFrames column-wise
print("\nColumn-wise Concatenation:")
print(pd.concat([df1, df2], axis=1))

# 6. Join DataFrames using their index
df1_index = df1.set_index('ID')
df2_index = df2.set_index('ID')

print("\nJoin:")
print(df1_index.join(df2_index, how='inner',
                     lsuffix='_left', rsuffix='_right'))