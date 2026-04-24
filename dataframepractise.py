
import pandas as pd
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
# }
# df = pd.DataFrame(data)
# print(df)

df = pd.read_csv('data.csv')
print(df.head())

subsetloc = df.loc[3:5, ['AQ', 'fail']]
print(subsetloc)

subsetiloc = df.iloc[3:6, 1:3]
print(subsetiloc)

hightemp = df[df['tempMode'] > 6]
print(hightemp)
# # print(df.shape)
# # print(df.dtypes)
# # print(df.describe())