df = pd.read_csv('1experience.csv')
description = df.describe()
quantitles = df['YearsExperience'].quantile([0.25, 0.5 , 0.75])
skewness = df['YearsExperience'].skew()
kurtosis = df['YearsExperience'].kurt()
value_counts = df['YearsExperience'].value_counts()
print("Statistical Summary:\n", description)
print("\nQuantiles:\n", qunatiles)
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)
print("\n Value Counts:\n", value_counts)

OUTPUT:
Statistical Summary:
       YearsExperience
count        10.000000
mean          4.300000
std           2.214722
min           1.000000
25%           2.250000
50%           4.500000
75%           5.750000
max           8.000000

Quantiles:
 0.25    2.25
0.50    4.50
0.75    5.75
Name: YearsExperience, dtype: float64

Skewness: 0.047
Kurtosis: -1.17

Value Counts:
2    2
5    2
1    1
3    1
4    1
6    1
7    1
8    1
Name: YearsExperience, dtype: int64
