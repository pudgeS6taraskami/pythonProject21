# На 3
import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

D = b**2 - 4*a*c
# Условные конструкции
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Корни уравнения:", x1, "и", x2)
elif D == 0:
    x = -b / (2*a)
    print("Уравнение имеет один корень:", x)
else:
    print("Уравнение не имеет корней.")

# на 4
a = 1
b = 2
c = 1

# Диапазон значений x
x_start = -5
x_stop = 5
x_step = 1

# Заголовок таблицы
print("{0:10} | {1:10}".format("x", "y"))
print("-" * 25)

# Таблица значений
for x in range(x_start, x_stop + x_step, x_step):
    y = a*x**2 + b*x + c
    print("{0:10} | {1:10}".format(x, y))

# На 5
import matplotlib.pyplot as plt
import numpy as np

# Коэффициенты параболы
a = 1
b = 2
c = 1

# Диапазон значений x
x_start = -5
x_stop = 5
x_step = 0.1

# Значения функции
x = np.arange(x_start, x_stop + x_step, x_step)
y = a*x**2 + b*x + c

# График
plt.plot(x, y)

# Добавляем заголовок и подписи к осям
plt.title("График параболы")
plt.xlabel("Ось x")
plt.ylabel("Ось y")

# Координатную сетку
plt.grid()

# Вывод графика на экран
plt.show()