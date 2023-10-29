from tkinter import *

#Función para agregar los numeros a un vector
def agregar_numeros():
    numeros = []  # Inicializamos un vector vacío para almacenar los números
    for entry in entrada_numeros:
        numero = entry.get()  # Obtenemos el valor del campo de entrada
        if not numero:  # Si el campo está vacío, agregamos 0
            numero = "0"
        numeros.append(float(numero))  # Convertimos el valor a float y lo agregamos al vector
    print("Números ingresados:", numeros)  # Puedes hacer lo que desees con el vector
    calcular_suma(numeros)
    contar_distintos(numeros)
    resultado_contar.config(text=f"10")
    calcular_promedio(numero)
#Función para realizar la suma de los 10 numeros 
def calcular_suma(numeros):
    suma = sum(numeros)
    resultado_label.config(text=f" {suma}")

#Función para contar los numeros distintos
def contar_distintos(numeros):
    numeros_distintos = set(numeros)  # Convierte la lista en un conjunto para obtener elementos únicos
    cantidad_distintos = len(numeros_distintos)
    resultado_distintos.config(text=f"{cantidad_distintos}")
    
#Def para el promedio
def calcular_promedio(numeros):
    if numeros:
        promedio = sum(numeros) / 10
        resultado_promedio.config(text=f"Promedio de los números: {promedio:.2f}")
    else:
        resultado_promedio.config(text="Promedio de los números: N/A")

ventana = Tk()
ventana.geometry("800x600")
ventana.title("Calculadora")
ventana.config(bg="#7AEBE8")

etq1 = Label(ventana, text="Bienvenido a esta calculadora")
etq1.config(font=("Arial", 12))
etq1.place(x=150, y=10, width=400, height=30)

etq2 = Label(ventana, text="Ingresa 10 numeros")
etq2.config(font=("Arial", 12))
etq2.place(x=40,y=50, width=150, height=30)

entrada_numeros = []  # Lista para mantener las referencias a los campos de entrada

for i in range(10):
    entrada = Entry(ventana)
    entrada.place(x=50, y=90 + i * 40, width=122, height=30)
    entrada_numeros.append(entrada)  # Agregamos cada campo de entrada a la lista

#Boton para ingresar los numeros
bt_ing = Button(ventana, text="Ingresar números", command=agregar_numeros)
bt_ing.place(x=50, y=490, width=122, height=30)

label_opera = Label(ventana, text="Operación")
label_opera.config(font=("Arial", 12))
label_opera.place(x=440, y=55, width=100, height=30)

label_result = Label(ventana, text="Resultado")
label_result.config(font=("Arial", 12))
label_result.place(x=550, y=55, width=200, height=30)

#Salida de la suma
label_Suma = Label(ventana, text="suma")
label_Suma.config(font=("Arial", 12))
label_Suma.place(x=440, y=90, width=100, height=30)

resultado_label = Label(ventana, text=" ")
resultado_label.config(font=("Arial", 12))
resultado_label.place(x=550, y=90, width=200, height=30)

#Salida de Contar distintos
label_distintos = Label(ventana, text="Distintos")
label_distintos.config(font=("Arial", 12))
label_distintos.place(x=440, y=130, width=100, height=30)

resultado_distintos= Label(ventana, text=" ")
resultado_distintos.config(font=("Arial", 12))
resultado_distintos.place(x=550, y=130, width=200, height=30)

#Salida de contar
label_contar = Label(ventana, text="Contar")
label_contar.config(font=("Arial", 12))
label_contar.place(x=440, y=170, width=100, height=30)

resultado_contar= Label(ventana, text=" ")
resultado_contar.config(font=("Arial", 12))
resultado_contar.place(x=550, y=170, width=200, height=30)

#Salida de promedio
label_promedio = Label(ventana, text="Promedio")
label_promedio.config(font=("Arial", 12))
label_promedio.place(x=440, y=210, width=100, height=30)

resultado_promedio= Label(ventana, text=" ")
resultado_promedio.config(font=("Arial", 12))
resultado_promedio.place(x=550, y=210, width=200, height=30)


ventana.mainloop()

