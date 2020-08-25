from tkinter import *
root=Tk()

miFrame=Frame(root, width=1200, height=600)
miFrame.pack()



nombreLabel=Label(miFrame, text="Nombre: ",padx=10, pady=10)
nombreLabel.grid(row=0,column=0, sticky="e")

passLabel=Label(miFrame, text="Contraseña: ",padx=10, pady=10)
passLabel.grid(row=1,column=0, sticky="e")

apellidoLabel=Label(miFrame, text="Apellidos: ",padx=10, pady=10)
apellidoLabel.grid(row=2,column=0, sticky="e")

direccionLabel=Label(miFrame, text="Direccion de casa: ",padx=10, pady=10)
direccionLabel.grid(row=3,column=0, sticky="e")

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4,column=0, sticky="e",padx=10, pady=10)


cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1,padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=1,column=1,padx=10, pady=10)
cuadroPassword.config(fg="red", justify="center", show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1,padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=10, pady=10)

textoComentario=Text(miFrame,width=20,height=5)
textoComentario.grid(row=4,column=1,padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4,column=2, sticky="nsew")


root.mainloop()