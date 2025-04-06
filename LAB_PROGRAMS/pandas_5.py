import pandas as pd


df = pd.read_csv(r'C:\SHANTI\RVU\Programs\Minors\IDA\Activities\Datasets\6Mcd_null_values.csv')

print("Original DataFrame:")
print(df)


print("\nMissing values before filling:")
print(df.isnull().sum())


df.fillna(df.mean(numeric_only=True), inplace=True)


df.drop_duplicates(inplace=True)


print("\nCleaned DataFrame (nulls filled, duplicates dropped):")
print(df)


print("\nMissing values after cleaning:")
print(df.isnull().sum())

OUTPUT:
Original DataFrame:
    Name    Q1   Q2
0   John   NaN  78
1   Lily  85.0  90
2   Mark  80.0  88
3   Rose   NaN  92
4   Lily  85.0  90

Missing values before filling:
Name    0
Q1      2
Q2      0
dtype: int64

Cleaned DataFrame (nulls filled, duplicates dropped):
    Name    Q1  Q2
0   John  82.5  78
1   Lily  85.0  90
2   Mark  80.0  88
3   Rose  82.5  92

Missing values after cleaning:
Name    0
Q1      0
Q2      0
dtype: int64

