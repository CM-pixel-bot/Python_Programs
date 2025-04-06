import pandas as pd
df=pd.read_csv('4laptops.csv)
df

pd.get_dummies(df)

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc_data = enc.fit_transform(df[['Category']])
enc_data 

enc.categories_

enc_data.toarray()

enc_df = pd.DataFrame(enc_data.toarray())
enc_df

enc_df = pd.DataFrame(enc_data.toarray(), columns = ['2 in 1 Convertible','Gaming','Notebook','Ultrabook','Workstation'])
enc_df

df1 = df.join(enc_df)
df1

from sklearn.preprocessing import labelEncoder
le = LabelEncoder()

df['RAM'] = le.fit_transform(df['RAM'])
df 

le.classes__





