import time
from tkinter import *

tk=Tk()
canvas=Canvas(tk, width=2000,height=600)
canvas.pack()

#image=PhotoImage(file="cancha.gif")
#canvas.create_image(0,0,anchor=NW, image=image)
arco=PhotoImage(file="arco_f.png")
canvas.create_image(900,45,anchor=NW, image=arco)
ball=PhotoImage(file="pelota.png")
canvas.create_image(50,90,anchor=NW, image=ball)

def movetriangle(event):
    canvas.move(2,10,-0.25)
    print(canvas.move("2","x","y"))
canvas.bind_all('<KeyPress-Return>',movetriangle)


#def funcion():
   #print ("GOOOOOOOOOOOOOOOOOOOOOOOOOOOLLL")
#tk=Tk()
#boton = tk.Button(tk, text="goooolll", command=funcion)
#boton.pack()

tk.mainloop()































































