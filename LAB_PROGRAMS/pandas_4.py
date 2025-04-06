import pandas as pd

df = pd.read_csv(r'C:\SHANTI\RVU\Programs\Minors\IDA\Activities\Datasets\6Mcd_null_values.csv')
print("Original DataFrame:")
df
print("\nMissing values in the DataFrame:")
print(df.isnull().sum())

df['Q1'].fillna(df['Q1'].mean(),inplace=True)

print("\nDataFrame after filling missing values in 'Q1' column:")
df

OUTPUT:
Original DataFrame:
   Name   Q1   Q2
0  John  NaN  78
1  Lily  85.0 90
2  Mark  80.0 88
3  Rose  NaN  92

Missing values in the DataFrame:
Name    0
Q1      2
Q2      0
dtype: int64

DataFrame after filling missing values in 'Q1' column:
   Name    Q1  Q2
0  John  82.5  78
1  Lily  85.0  90
2  Mark  80.0  88
3  Rose  82.5  92
