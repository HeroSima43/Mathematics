# Условие 3
# Проведите тест гипотезы.
# Продавец утверждает, что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать,
# что доверительная вероятность равна 99%? (Провести двусторонний тест.)

from math import sqrt


def average(list):
    sum = 0
    for i in list:
        sum = sum + i
    avr = sum / len(list)
    return avr


def unbiased_variance(list):    # Функция нахождения несмещенной дисперсии
    sum = 0
    for i in list:
        sum = sum + (i - average(list)) ** 2
    uv = sum / (len(list) - 1)
    return uv


pack_weight = 200
sample = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]

tn = (average(sample) - pack_weight) / (sqrt(unbiased_variance(sample)) / sqrt(len(sample)))

tt = 3.25   # Значение по таблице Стьюдента (уровень значимости 0,01, степень свободы 9)
if abs(tn) < tt:
    print(f"Утверждение верно, так как наблюдаемое значение: {round(abs(tn), 4)} меньше критической точки: {tt}")
else:
    print(f"Утверждение НЕ верно, так как наблюдаемое значение: {abs(tn)} больше критической точки: {tt}")
