from tkinter import *
from time import sleep

class Text:
    def __init__(self, x, y, text, color, font, size):
        self.font, self.size, self.id = font, size, back.create_text(x,y,text=text,fill=color,font=(font,size))
    def resize(self):
        self.size*=2 if fullsize else 0.5
        back.itemconfig(self.id, font=(self.font,int(self.size)))

root = Tk()
root.title('点阵争霸')
root.geometry('960x540')
root.resizable(False, False)
# root.iconphoto(True, PhotoImage(file=''))
back = Canvas(root, bg='black', highlightthickness=0)
back.pack(fill=BOTH, expand=True)
screen1,screen2=[Text(300,300,'hello','white','方正兰亭粗黑简体',40)],[]
fullsize=0
def change(e):
    global fullsize
    fullsize=1 if fullsize==0 else 0
    screen1[0].resize()
root.bind('<Button-1>', change)

root.mainloop()