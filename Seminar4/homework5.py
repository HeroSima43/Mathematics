# Условие 5.
# На сколько сигм (средних квадратичных отклонений) отклоняется рост человека,
# равный 190 см, от математического ожидания роста в популяции,
# в которой M(X) = 178 см и D(X) = 25 кв.см?

from math import sqrt

m = 178
d = 25
x = 190

sigma = (x - m) / sqrt(d)
print(f"Ответ: {sigma}")
