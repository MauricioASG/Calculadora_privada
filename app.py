from tkinter import *

ventana = Tk()
ventana.geometry("800x600")
ventana.title("Calculadora")
ventana.config(bg="#7AEBE8")

etq1 = Label(ventana, text="Bienvenido a esta aplicación")
etq1.config(font=("Arial", 12))
etq1.place(x=150, y=10, width=400, height=30)


ent1 = Entry(ventana)
ent1.place(x=50, y=50, width=122, height=30)

ent2 = Entry(ventana)
ent2.place(x=50, y=90, width=122, height=30)

ent3 = Entry(ventana)
ent3.place(x=50, y=130, width=122, height=30)

ent4 = Entry(ventana)
ent4.place(x=50, y=170, width=122, height=30)

ent5 = Entry(ventana)
ent5.place(x=50, y=210, width=122, height=30)

ent6 = Entry(ventana)
ent6.place(x=50, y=250, width=122, height=30)

ent7= Entry(ventana)
ent7.place(x=50, y=290, width=122, height=30)

ent8 = Entry(ventana)
ent8.place(x=50, y=330, width=122, height=30)

ent9 = Entry(ventana)
ent9.place(x=50, y=370, width=122, height=30)

ent10 = Entry(ventana)
ent10.place(x=50, y=410, width=122, height=30)

bt_ing = Button(ventana, text="Ingresar números")
bt_ing.place(x=50, y=450, width=122, height=30)



ventana.mainloop()

