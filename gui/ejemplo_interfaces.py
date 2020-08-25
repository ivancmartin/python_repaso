from tkinter import *
raiz=Tk()
raiz.title("Ventana de prueba")
raiz.resizable(1,1)
#raiz.geometry("650x350") la raiz siempre se adapta al frame, no es necesario darle tamaño
raiz.config(bg='grey')
#raiz.iconbitmap("icono.ico")

miFrame=Frame()
miFrame.pack(fill="y", expand="true")
miFrame.config(bg="green",width="650",height="350")

miFrame.config(bd=5)
miFrame.config(relief="groove")

miFrame.config(cursor="pirate")
raiz.mainloop()#Esta instruccion simepre se coloca al final
