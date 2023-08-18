import numpy as np
import pandas as pd

data = {
    'Ім\'я': ['Анна', 'Борис', 'Вікторія', 'Дмитро', 'Еліза'],
    'Вік': [25, 32, 28, 22, 29],
    'Зарплата': [50000, 60000, 55000, 48000, 52000]
}

df = pd.DataFrame(data)

print("Початковий DataFrame:")
print(df)

df['Досвід роботи (роки)'] = np.random.randint(1, 6, size=len(df))

середня_зарплата = df['Зарплата'].mean()
print("\nСередня зарплата:", середня_зарплата)

df_сорт_вік = df.sort_values(by='Вік')
print("\nВідсортований DataFrame за віком:")
print(df_сорт_вік)

df_вибірка = df[(df['Вік'] < 30) & (df['Зарплата'] > середня_зарплата)]
print("\nВибірка рядків за умовою:")
print(df_вибірка)
