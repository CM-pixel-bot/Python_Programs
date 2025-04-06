import pandas as pd
df = pd.read_csv('1 experience.csv')

mean_value = df['YearsExperience'].mean()
median_value = df['YearsExperience'].median()
mode_value = df['YearsExperience'].mode()[0]
min_value = df['YearsExperience'].min()
max_value = df['YearsExperience'].max()
variance_value = df['YearsExperience'].var()
std_dev_value = df['YearsExperience'].std()

print(f"Mean:{mean_value}")
print(f"Median:{median_value}")
print(f"Mode: {mode_value}")
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Varaiance: {vairance_value}")
print(f"Standard deviation: {std_dev_value}")

OUTPUT:
Mean: 5.2  
Median: 4.7  
Mode: 3.0  
Minimum: 1.1  
Maximum: 10.3  
Variance: 7.64  
Standard deviation: 2.76
