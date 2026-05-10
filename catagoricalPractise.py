import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('healthcare_patient_analytics_seaborn.csv')
 
#  Sample of 500 rows
df_sample = df.sample(n=500)

# 1. Countplot for '
# sns.countplot(data=df_sample, x='treatment_type')
# sns.barplot(data=df_sample, x='department',y='treatment_cost')
sns.boxplot(data=df_sample, x='department', y='recovery_score')
# sns.violinplot(data=df_sample, x='department', y='recovery_score')
sns.stripplot(data=df_sample, x='department', y='recovery_score',color='blue',alpha=0.4)  # Add jitter for better visibility of data points
# plt.title('Recovery Score by Department')
plt.xticks(rotation=30)
plt.show()