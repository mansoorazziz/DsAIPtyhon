import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('healthcare_patient_analytics_seaborn.csv')

# sns.histplot(data=df, x='treatment_cost', bins=30) 
# sns.histplot(data=df, x='readmission_risk',hue='visit_type',multiple='stack', bins=30)
# sns.kdeplot(data=df, x='recovery_score', hue='visit_type', fill=True)
sns.ecdfplot(data=df, x='length_of_stay_days', hue='visit_type')
plt.title('Length of Stay by Visit Type')
plt.show()

# df = sns.load_dataset('healthcare_patient_analytics_seaborn')
