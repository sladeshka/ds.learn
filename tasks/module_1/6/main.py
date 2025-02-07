import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression

df = pd.read_csv('data_hw_reg.csv', parse_dates=['date'])
"""Display statistics"""
df.head()
df.info()
"""No skips, no outliers"""

"""Filtering data by country"""
df_russia = df[df['country'] == 'Russia']
df_us = df[df['country'] == 'US']

"""Calculation of the correlation coefficient"""
correlation = df['confirmed'].corr(df['deaths'])
print(f"Correlation coefficient between morbidity and mortality {correlation:.4f}.")

"""Visualization of the graph"""
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='date', y='confirmed', hue='country', marker='o',)
sns.lineplot(data=df, x='date', y='deaths', hue='country', marker='.')
plt.title('Dynamics of morbidity and mortality by country')
plt.xlabel('Date')
plt.ylabel('Quantity')
plt.legend(['Morbidity Rus', 'Mortality Rus', 'Morbidity Us', 'Mortality Us'])
plt.show()

"""Clearing the data and preparing data for linear regression"""
df_cleaned = df.dropna()
X = df_cleaned['confirmed'].values.reshape(-1, 1)
y = df_cleaned['deaths'].values

"""Building a linear regression"""
model = LinearRegression()
model.fit(X, y)

"""Projected number of deaths for 25000000 infections"""
slope = model.coef_[0]
intercept = model.intercept_
predicted_deaths = model.predict(np.array([[25000000]]))
print(f"Projected number of deaths for 25,000,000 infections: {predicted_deaths[0]:.2f}")
