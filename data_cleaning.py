import pandas as pd
import csv

df = pd.read_csv('total_stars.csv')
print(df)
print(df.columns)

df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity', 'id'],axis=1,inplace=True)
print(df)


final_data = df.dropna()
print(final_data)
final_data.reset_index(drop=True,inplace = True)
print(final_data)

final_data.to_csv('final_data.csv')
print(final_data.info())
print(final_data.describe())
print(final_data.head(5))
print(final_data.dtypes)

