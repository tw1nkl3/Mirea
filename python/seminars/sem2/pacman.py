from tkinter import *

# создаем окно
root = Tk()
root.title("Pacman")

# создаем поле для рисования
canvas = Canvas(root, width=300, height=300, bg="black")
canvas.pack()

# рисуем круг
x = 150
y = 150
r = 100
canvas.create_oval(x-r, y-r, x+r, y+r, fill="black", outline="black")

# рисуем рот
canvas.create_arc(x-r, y-r, x+r, y+r, start=30, extent=300, fill="yellow", outline="black")

# рисуем глаза
canvas.create_oval(x-r/2, y-r/2, x-r/4, y-r/4, fill="black", outline="white")
canvas.create_oval(x+r/4, y-r/2, x+r/2, y-r/4, fill="black", outline="white")

# запускаем главный цикл
root.mainloop()
