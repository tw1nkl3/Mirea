import tkinter as tk

# создаем окно
root = tk.Tk()

# создаем холст (canvas) на котором будем рисовать
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# рисуем круг с координатами (100, 100) и радиусом 50
circle = canvas.create_oval(50, 50, 150, 150, outline='black', fill='red')

# запускаем главный цикл приложения
root.mainloop()
