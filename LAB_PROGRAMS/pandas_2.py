import pandas as pd
df = pd.read_csv('1 experience.csv')
print("First 6 rows of the DataFrame:")
print(df.head(6))
print('\nColumn names and data types:")
print(df.info())

Output:
      Name  Experience Department
0    Alice           2    Finance
1      Bob           5         HR
2  Charlie           3  Marketing
3    David           6         IT
4     Emma           1      Sales
5     Fred           4         HR

Name          object
Experience     int64
Department     object
dtype: object

