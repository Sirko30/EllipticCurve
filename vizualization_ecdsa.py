import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("prepared_table.csv")

df_filtered = df[~df['curve_type'].str.contains("Ed")]

print(df.head())

sns.set(style="whitegrid")

plt.figure(figsize=(8, 6))
sns.lineplot(data=df_filtered, x='bit_size', y='keygen/s', hue='curve_type', marker='o')

plt.title('Порівняння продуктивності генерації ключів для різних типів кривих', fontsize=14)
plt.xlabel('Розрядність ключа (біт)', fontsize=12)
plt.ylabel('Кількість пар ключів/с', fontsize=12)
plt.legend(title='Тип кривої', fontsize=10)
plt.show()

plt.figure(figsize=(8, 6))
sns.lineplot(data=df_filtered, x='bit_size', y='sign/s', hue='curve_type', marker='o')

plt.title('Порівняння продуктивності підпису для різних типів кривих', fontsize=14)
plt.xlabel('Розрядність ключа (біт)', fontsize=12)
plt.ylabel('Кількість підписів/с', fontsize=12)
plt.legend(title='Тип кривої', fontsize=10)
plt.show()

plt.figure(figsize=(8, 6))
sns.lineplot(data=df_filtered, x='bit_size', y='verify/s', hue='curve_type', marker='o')

plt.title('Порівняння продуктивності перевірки підпису для різних типів кривих', fontsize=14)
plt.xlabel('Розрядність ключа (біт)', fontsize=12)
plt.ylabel('Кількість перевірок/с', fontsize=12)
plt.legend(title='Тип кривої', fontsize=10)
plt.show()
