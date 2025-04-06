import pandas as pd
df = pd.read_csv(r"3Salary_Data.csv")
df
from sklearn.preprocessing import StandardScaler

scaler = StandadrdScaler()
scaled_data = scaler.fit_transform(df)
scaled_df1 = pd.DataFrame(scaled_data, columns = df.columns)
scaled_df1

OUTPUT:
YearsExperience	Salary
-1.46         	-1.42
-1.13         	-1.19
-0.80	          -0.87
...	             ...
1.72	           1.82

