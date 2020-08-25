from tkinter import *
root=Tk()

miFrame=Frame(root,width="500",height="400")
miFrame.pack()

miImagen=PhotoImage(file="monete.gif")

#Label(miFrame,text="Hola a todos", bg="green", fg="red", font=("Comic Sans MS",20)).place(x=100,y=200)
Label(miFrame,image=miImagen).place(x=0,y=0)

root.mainloop()