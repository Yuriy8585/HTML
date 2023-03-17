import pandas as pd

df = pd.read_csv('https://storage.googleapis.com/mledu-datasets/california_housing_train.csv')
# print(df.head(n = 10))
# print(df.tail(n = 2))
# print(df.shape)
# print(df.isnull().sum())
# print(df.dtypes)
# print(df.columns)
# print(df[['latitude', 'population']])
# print(df[df['housing_median_age']< 20])
# print(df[(df['housing_median_age'] < 20) & (df['housing_median_age'] > 10)][['total_rooms', 'population']])
# print(df['population'].max())
# print(df[['population', 'total_rooms']].median())
# print(df.describe())



import seaborn as sns
#sns.scatterplot(data = df, x = 'longitude', y = 'latitude')

#sns.scatterplot(data=df, x = 'households', y = 'population', hue = 'total_rooms')

# sns.scatterplot(data=df, x = 'households', y = 'population', hue = 'total_rooms', size=10)

#cols = ['population', 'median_income', 'housing_median_age', 'median_house_value']
#g = sns.PairGrid(df[cols])
#g.map(sns.scatterplot)

#sns.relplot(x = 'latitude', y = 'median_house_value', kind='line', data=df)

#sns.histplot(data=df, x = 'median_income')

#sns.histplot(data=df, x = 'housing_median_age')

#sns.histplot(data=df[df['housing_median_age']>50], x='median_income')

df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50),
'age_group'] = 'Ср. возраст'
df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'

#df.groupby('age_group')['median_income'].mean().plot(kind='bar')

df.loc[df['median_income'] > 6, 'income_group'] = 'rich'
df.loc[df['median_income'] < 6, 'income_group'] = 'everyone_else'

sns.displot(df, x="median_house_value", hue="income_group")