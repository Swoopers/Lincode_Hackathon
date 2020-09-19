import time
from tkinter import *
import math
import json

tk=Tk()
tk.title("Drawing")
display_width = 800
display_height = 800

canvas=Canvas(tk,width=display_width,height=display_height)
canvas.pack()
distance = 180
with open('lidar.json') as f:
    data = json.load(f)


for i in range(len(data)):
	canvas.create_line(400,400,400 + math.cos(math.radians(i-90))*data[str(i)]*4,400 + math.sin(math.radians(i-90))*data[str(i)]*4)
	tk.update()
tk.mainloop() 