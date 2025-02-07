import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats

df = pd.read_csv('FPS_hw_x_df_x_taxi2.csv', sep=";")
"""Display statistics"""
df.head()
df.info()
"""No skips, no outliers"""

"""Filtering data by type"""
economy_distances = df[df['offer_class_group'] == 'Economy']['distance_km']
comfort_distances = df[df['offer_class_group'] == 'Comfort']['distance_km']

"""Descriptive statistics for economy class"""
economy_distances.describe()
"""Descriptive statistics for comfort class"""
comfort_distances.describe()

economy_distances = pd.to_numeric(economy_distances, errors='coerce')
comfort_distances = pd.to_numeric(comfort_distances, errors='coerce')

economy_distances = economy_distances.dropna()
comfort_distances = comfort_distances.dropna()

"""Distribution density graphs"""
plt.figure(figsize=(8, 5))
sns.kdeplot(economy_distances, label='Economy', fill=True, color='green', alpha=0.5)
sns.kdeplot(comfort_distances, label='Comfort', fill=True, color='red', alpha=0.5)
plt.title('Distribution density of travel distances')
plt.xlabel('Distance')
plt.ylabel('Density')
plt.legend()
plt.show()

"""Hypothesis testing"""
"""H0 = For long-distance travel users there is no difference in class"""
"""H1 = For long trips, users prefer the more comfortable travel conditions in the Comfort class to the Economy class"""
t_stat, p_value = stats.ttest_ind(economy_distances, comfort_distances, equal_var=True)

print(f"T-statistic: {t_stat}, P-value: {p_value}")

"""Significance level"""
if p_value < 0.05:
    print("Rejecting the null hypothesis")
else:
    print("Confirming the null hypothesis")
