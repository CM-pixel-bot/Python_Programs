import pandas as pd

data = {'Name': ['Alice','Bob','Charlie','David']
        'Age' : [25, 30, 35, 40]
        'Salary': [50000, 60000, 70000, 80000]}
df = pd.DataFrame(data)
print("DataFrame from Scratch:")
print(df)
df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame after adding 'Bonus' column:")
print(df)

OUTPUT:
DataFrame from Scratch:
     Name  Age  Salary
0   Alice   25   50000
1     Bob   30   60000
2 Charlie   35   70000
3   David   40   80000

DataFrame after adding 'Bonus' column:
     Name  Age  Salary   Bonus
0   Alice   25   50000  5000.0
1     Bob   30   60000  6000.0
2 Charlie   35   70000  7000.0
3   David   40   80000  8000.0

