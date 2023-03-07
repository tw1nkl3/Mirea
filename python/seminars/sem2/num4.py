from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Цвета")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_oval(
            10, 10, 300, 300, 
            fill="#FFC300"
        )

        canvas.create_line(155, 185, 255, 185, 205, 280, 155, 185)


        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("325x325+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()