from tkinter import *
import random
import time

class Menu:#Это оно самое 
    
    
    def __init__(self, tk, win, label1):
        def game_start(self, tk):
            win = Toplevel(tk)
            label1 = Label(win, text="Start")
            label1.pack()

        def exit_app(self, tk):
            tk.destroy()


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.cavas_height = self.canvas.winfo_height()
        self.cavas_width = self.canvas.winfo_width()
        self.hit_button = False
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.cavas_height:
            self.hit_button = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.cavas_width:
            self.x = -3
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.cavas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.cavas_width:
            self.x = 0
    def turn_left(self, evt):
        self.x = -2.5
    def turn_right(self, evt):
        self.x = 2.5
tk = Tk()
tk.title("BPRNS(1)")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
main_menu = Menu(tk)#
tk.configure(menu=main_menu)
first_item = Menu(main_menu)
main_menu.add_cascade(label="file", menu=first_item)
first_item.add_command(label="New_Game", command=game_start)
first_item.add_command(label="Exit", command=exit_app)
tk.mainloop()
paddle = Paddle(canvas, "pink")
ball = Ball(canvas, paddle, "violet")

while 1:
    if ball.hit_button == False:
        ball.draw()
        paddle.draw()
    elif ball.hit_button == True:
        canvas.create_text(250, 200, text="You lose. This is end. Press <X> to close program.", fill="red", font=12)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)
