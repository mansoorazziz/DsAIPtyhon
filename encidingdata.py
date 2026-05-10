import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# df = pd.DataFrame({
#     'City': ['New York', 'London', 'New York', 'Paris', 'London'],
#     'Segment': ['A', 'B', 'A', 'D', 'C'],
#     'Sales': [100, 150, 200, 250, 300]
# })
df2 = pd.DataFrame({'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small']})
encoder = OrdinalEncoder(categories=[['Small', 'Medium', 'Large']])
df2['Size_encoded'] = encoder.fit_transform(df2[['Size']])

print(df2)
# One-Hot Encoding
# one_hot_encoded = pd.get_dummies(df, columns=['City' , 'Segment'],drop_first=False)
# print(one_hot_encoded)
# one_hot_encoded = pd.get_dummies(df['City'])pip