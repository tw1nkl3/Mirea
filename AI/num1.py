import random
import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin, log, e
from matplotlib import pyplot as plt
import numpy as np
import math
import numpy as np
import matplotlib. pyplot as plt
from scipy. integrate import simps
from numpy import trapz


""" x = 5 >= 2
A = {1, 3, 7, 8}
B = {2, 4, 5, 10, 'apple'}
C = A & B
df = 'Антонова Антонина', 34,
z = 'type'
D = [1, 'title', 2, 'content']

print(x,'|', type(x),'\n',  z, '|', type(z),'\n', 
      df, '|', type(df), '\n', A, '|', type(A)) """


""" x = int(input())

if x < -5:
    print('(-inf; -5)')
elif -5 <= x <= 5:
    print('[-5; 5]')
else:
    print('(5; +inf)') """


""" x = 10
while x >= 1:
    print(x)
    x -= 3 """


""" arr = ['имя', 'фамилия', 'возраст', 'вес', 'пол']
print(arr) """


""" arr = []
for i in range(2, 16, 1):
    arr.append(i)
print(arr) """


""" arr = []
for i in range(105, 4, -25):
    arr.append(i)
print(arr) """


""" x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x[0::2] = reversed(x[0::2])
print(x) """


""" def main(x):
    f1 = e ** ((x)**0.5)
    f2 = (1 + f1 + (cos(x))**2)**0.5
    f3 = abs(1 - (sin(x)**3))
    f4 = f2 / f3
    f5 = log(abs(2*x))
    return f4 + f5
mass = range(1,10,1)
for i in mass:
    a[i] = main(i)
ac = a[:50]
print(ac,'\n',list(a))
plt.grid()
plt.plot(range(10), a, c = "r")
plt.fill_between(range(10),a)
plt.grid()
plt.scatter(range(5), ac)
plt.show() """


""" Apple = [131.99, 121.88, 122.18, 131.5, 124.67, 137.02, 145.84, 151.92, 141.71, 149.87, 166.44, 177.51]

Microsoft = [231.79, 232.42, 237.55, 252.12, 250, 270.98, 285, 302.14, 282.26, 331.83, 333.49, 336.27]

Google =[91.35, 101.1, 103.2, 117.88, 117.85, 122.1, 134.7, 144.83, 133.78, 148, 142.76, 145.05]

mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

plt.plot(mes, Microsoft, c = "r")
plt.plot(mes, Apple, c = "g")
plt.plot(mes, Google, c = "b")
plt.grid()
plt.show() """


""" # создаем массив случайных значений из интервала (0; 1)
data = np.random.rand(100)

# вычисляем среднее значение и медиану
mean_value = np.mean(data)
median_value = np.median(data)

# выводим результаты
print("Среднее значение: ", mean_value)
print("Медиана: ", median_value)

# строим точечную диаграмму рассеяния
plt.scatter(range(len(data)), data)
plt.xlabel("Индекс элемента")
plt.ylabel("Значение")
plt.title("Точечная диаграмма рассеяния")
plt.show() """


""" def calculator():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. e^(x+y)")
    print("6. sin(x+y)")
    print("7. cos(x+y)")
    print("8. x^y")
    
    choice = input("Введите номер операции (1-8): ")
    
    if choice in ('1', '2', '3', '4', '8'):
        x = float(input("Введите первое число: "))
        y = float(input("Введите второе число: "))
        
        if choice == '1':
            print(x, "+", y, "=", x + y)
        
        elif choice == '2':
            print(x, "-", y, "=", x - y)
        
        elif choice == '3':
            print(x, "*", y, "=", x * y)
        
        elif choice == '4':
            if y != 0:
                print(x, "/", y, "=", x / y)
            else:
                print("Ошибка: деление на ноль")
        
        elif choice == '8':
            print(x, "^", y, "=", x ** y)
            
    elif choice in ('5', '6', '7'):
        x = float(input("Введите значение угла в градусах: "))
        y = float(input("Введите значение угла в градусах: "))
        x_rad = math.radians(x)
        y_rad = math.radians(y)
        
        if choice == '5':
            print("e^(", x, "+", y, ")=", math.exp(x_rad+y_rad))
        
        elif choice == '6':
            print("sin(", x, "+", y, ")=", math.sin(x_rad+y_rad))
        
        elif choice == '7':
            print("cos(", x, "+", y, ")=", math.cos(x_rad+y_rad))
            
    else:
        print("Некорректный ввод")

calculator() """


""" x = np.arange(1,10,1)
y = np.abs(np.fabs(np.cos(x*np.exp(np.cos(x)+np.log(x+1)))))
plt.grid()
plt.plot(x,y,c= "r")
plt. fill_between(x,y)
area = trapz(y)
print(area)
data = np.random.rand(100)

# строим точечную диаграмму рассеяния
plt.scatter(range(len(data)), data)
plt.xlabel("Индекс элемента")
plt.ylabel("Значение")
plt.title("Точечная диаграмма рассеяния")
plt.show() """