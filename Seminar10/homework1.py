# Условие 1
# Провести дисперсионный анализ для определения того, есть ли различия
# среднего роста среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

import numpy as np
from scipy import stats

y1 = np.array([173, 175, 180, 178, 177, 185, 183, 182])
y2 = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
y3 = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

n1 = len(y1)
n2 = len(y2)
n3 = len(y3)
k = 3   # Количество групп

y1_mean = np.mean(y1)
print(f"Средний рост футболистов: {round(y1_mean, 2)}")
y2_mean = np.mean(y2)
print(f"Средний рост хоккеистов: {round(y2_mean, 2)}")
y3_mean = np.mean(y3)
print(f"Средний рост штангистов: {round(y3_mean, 2)}")

total = np.concatenate([y1, y2, y3])

total_mean = np.mean(total)
print(f"Средний рост всех спортсменов: {round(total_mean, 2)}")

s = np.sum((total - total_mean)**2)
print(f"Сумма квадратов отклонений наблюдений от общего среднего: {round(s, 2)}")

s_f = n1 * (np.sum(y1_mean - total_mean)**2) + n2 * (np.sum(y2_mean - total_mean)**2) + n3 * (np.sum(y3_mean - total_mean)**2)
print(f"Сумма квадратов отклонений средних групповых значений от общего среднего: {round(s_f, 2)}")

s_ost = np.sum((y1 - y1_mean)**2) + np.sum((y2 - y2_mean)**2) + np.sum((y3 - y3_mean)**2)
print(f"Остаточная сумма квадратов отклонений: {round(s_ost, 2)}")

D_f = s_f / (k - 1)
print(f"Факторная дисперсия: {round(D_f, 2)}")

D_ost = s_ost / (len(total) - k)
print(f"Остаточная дисперсия: {round(D_ost, 2)}")
F_n = D_f / D_ost
print(f"Критерий Фишера: {round(F_n, 2)}")

# Табличное значение критерия Фишера:
# Уровень статистической значимости = 0.05
# (k - 1) = 3 - 1 = 2 Степени свободы числителя
# (n - k) = 28 - 3 = 25 Степеней свободы знаменателя
F_t = 3.38

if F_n < F_t:
    print(f"Так как наблюдаемое значение: {round(F_n, 2)} меньше критической точки: {F_t} \n"
          "отличие среднего роста спортсменов НЕ является статистически значимым")
else:
    print(f"Так как наблюдаемое значение: {round(F_n, 2)} больше критической точки: {F_t} \n"
          "отличие среднего роста спортсменов является статистически значимым")