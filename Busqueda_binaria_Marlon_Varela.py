import tkinter as tk

def agregar_numero():
    numero = int(entry1.get())
    arreglo.append(numero)
    label_lista.config(text=str(arreglo))
    entry1.delete(0,tk.END)

def busqueda_binaria(arreglo, numero):
    inicio = 0
    fin = len(arreglo) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        numero_medio = arreglo[medio]

        if numero_medio == numero:
            return medio
        elif numero_medio < numero:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

def buscar_numero():
    numero = int(entry2.get())
    resultado = busqueda_binaria(arreglo, numero)

    if resultado == -1:
        label_resultado.config(text="El número no fue encontrado.")
    else:
        label_resultado.config(text=f"El número {numero} se encuentra en la posición {resultado}.")
    entry2.delete(0,tk.END)

ventana = tk.Tk()
ventana.geometry("350x230")
ventana.title("Búsqueda Binaria - Marlon Varela")

label_lista = tk.Label(ventana, text = " ")
label_lista.pack()

label1 = tk.Label(ventana, text = "Ingrese numeros a la lista")
label1.pack()

entry1 = tk.Entry(ventana)
entry1.pack()

boton1 = tk.Button(ventana, text="Agregar", command=agregar_numero)
boton1.pack()

labelinv = tk.Label(ventana, text= " ")
labelinv.pack()

label2 = tk.Label(ventana, text="Ingrese un numero para buscar:")
label2.pack()

entry2 = tk.Entry(ventana)
entry2.pack()

button2 = tk.Button(ventana, text="Buscar", command=buscar_numero)
button2.pack()

label_resultado= tk.Label(ventana, text=" ")
label_resultado.pack()

arreglo = []

ventana.mainloop()
