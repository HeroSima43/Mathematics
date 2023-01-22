# Условие 1.
# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение,
# смещенную и несмещенную оценки дисперсий для данной выборки.

from math import sqrt

my_list = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

# Посчитать среднее арифметическое


def average(list):
    sum = 0
    for i in list:
        sum = sum + i
    avr = sum / len(list)
    return avr


print(f"Среднее арифметическое: {average(my_list)}")

# Посчитать среднее квадратичное отклонение


def sum_of_squared_deviations(list):        # Рассчитаем сумму квадратов отклонений значений относительно среднего
    sum = 0
    for i in list:
        sum = sum + (i - average(list)) ** 2
    return sum


standard_deviation = sqrt(sum_of_squared_deviations(my_list) / len(my_list))
print(f"Среднее квадратичное отклонение: {standard_deviation}")

# Посчитать смещенную дисперсию

shifted_variance = sum_of_squared_deviations(my_list) / (len(my_list))
print(f"Смещенная дисперсия: {shifted_variance}")

# Посчитать несмещенную дисперсию

unbiased_variance = sum_of_squared_deviations(my_list) / (len(my_list) - 1)
print(f"Несмещенная дисперсия: {unbiased_variance}")
