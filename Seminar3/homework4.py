# Условие 4.
# В университет на факультеты A и B поступило равное количество студентов,
# а на факультет C студентов поступило столько же, сколько на A и B вместе.
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7,
# а для студента факультета C - 0.9. Студент сдал первую сессию.
# Какова вероятность, что он учится:

p1 = 0.8
p2 = 0.7
p3 = 0.9

p0 = 1/4 * p1 + 1/4 * p2 + 1/2 * p3      # Вероятность того, что студенты всех факультетов сдадут сессию

# a). на факультете A

p = (1/4 * p1) / p0
print(f"Вероятность, что он учится на факультете А: {round(p, 4)} или {round(p * 100, 2)} %")

# б). на факультете B

p = (1/4 * p2) / p0
print(f"Вероятность, что он учится на факультете В: {round(p, 4)} или {round(p * 100, 2)} %")

# в). на факультете C

p = (1/2 * p3) / p0
print(f"Вероятность, что он учится на факультете С: {round(p, 4)} или {round(p * 100, 2)} %")