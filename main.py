import pandas as pd
import numpy as np

# 1. Создание DataFrame (10 учеников × 5 предметов)
np.random.seed(42)
subjects = ['Математика', 'Русский язык', 'Физика', 'История', 'Английский']
student_names = [f'Ученик_{i+1}' for i in range(10)]
data = {subject: np.random.randint(2, 6, 10) for subject in subjects}
data['ФИО'] = student_names
df = pd.DataFrame(data)[['ФИО'] + subjects]

# 2. Проверка первых строк DataFrame
print('Первые строки:')
print(df.head(), end='\n\n')

# 3. Средние оценки по предметам
print('Средние оценки:')
print(df[subjects].mean(), end='\n\n')

# 4. Медианные оценки по предметам
print('Медианные оценки:')
print(df[subjects].median(), end='\n\n')

# 5. Q1, Q3 и IQR по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(f"Q1 (Математика): {Q1_math}")
print(f"Q3 (Математика): {Q3_math}")
print(f"IQR (Математика): {IQR_math}\n")

# 6. Стандартное отклонение по предметам
print('Стандартное отклонение:')
print(df[subjects].std())
