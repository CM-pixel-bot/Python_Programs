import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('2Salary.csv')


print("Experience Statistics:\n")
print(df['YearsExperience'].describe())
print("\nSkewness:", df['YearsExperience'].skew())
print("Kurtosis:", df['YearsExperience'].kurt())


plt.hist(df['YearsExperience'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Employee Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Number of Employees')
plt.grid(True)
plt.show()

OUTPUT:
Experience Statistics:

count     10.000000
mean       4.700000
std        2.625262
min        1.200000
25%        2.675000
50%        4.500000
75%        6.625000
max        9.200000
Name: YearsExperience, dtype: float64

Skewness: 0.256
Kurtosis: -1.030
