import tkinter as tk
import random

# Функция, которая будет вызвана при щелчке мышью в окне
def noise(event):
    x, y = event.x, event.y  # Получаем координаты щелчка мышью
    value = random.random()  # Генерируем случайное значение
    print(f"Шум в ({x}, {y}): {value}")  # Выводим результат

# Создаем окно
root = tk.Tk()

# Задаем размер окна
root.geometry("400x400")

# Создаем холст, на котором будут отображаться значения
canvas = tk.Canvas(root, width=400, height=400)

# Привязываем функцию noise к событию щелчка мышью
canvas.bind("<Button-1>", noise)

# Размещаем холст в окне
canvas.pack()

# Запускаем главный цикл окна
root.mainloop()
