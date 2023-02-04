# Условие 1
# Даны две независимые выборки. Не соблюдается условие нормальности
# x1 380,420, 290
# y1 140,360,200,900
# Сделайте вывод по результатам, полученным с помощью функции

import scipy.stats as stats

x1 = [380, 420, 290]
y1 = [140, 360, 200, 900]

print(stats.mannwhitneyu(x1, y1))
print("p-value = 0.629, что дает нам право сделать выбор в пользу нулевой гипотезы, т.к. даже при альфа=0.1 p-value > альфа")
