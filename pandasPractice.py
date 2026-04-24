import pandas as pd
# print('imported pandas successfully')

s = pd.Series([1, 2, 1, 4, 5], index=['a', 'b', 'c', 'd', 'e']  )
print(s)
print(s.values)
print(s.index)
print(s.dtype  )

print(s.head)
print(s.tail)

print(s.value_counts())