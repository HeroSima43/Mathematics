# Условие 5
# Заявляется, что партия изготавливается со средним арифметическим 2,5 см.
# Проверить данную гипотезу, если известно, что размеры изделий
# подчинены нормальному закону распределения.
# Объем выборки 10, уровень статистической значимости 5%
# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34

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


m = 2.5
sample = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
tt = 2.262   # Значение по таблице Стьюдента (уровень значимости 0,05, степень свободы 9)

tn = (average(sample) - m) / (sqrt(unbiased_variance(sample)) / sqrt(len(sample)))
if abs(tn) < tt:
    print(f"Утверждение верно, так как наблюдаемое значение: {round(abs(tn), 4)} меньше критической точки: {tt}")
else:
    print(f"Утверждение НЕ верно, так как наблюдаемое значение: {abs(tn)} больше критической точки: {tt}")
