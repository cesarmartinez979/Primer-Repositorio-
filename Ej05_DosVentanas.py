#CBTIS 89
#3°B PROGRAMACION MATUTINO 
#CESAR ARMANDO MARTINEZ COVARRUBIAS



import tkinter as tk
from tkinter import Toplevel

def abrir_ventana1():
    ventana1 = Toplevel()
    ventana1.title("Ventana 1")
    ventana1.geometry("300x150")
    tk.Label(ventana1, text="Nombre: Armando", font=("Arial", 12)).pack(pady=10)
    tk.Label(ventana1, text="Apellido: Martínez", font=("Arial", 12)).pack(pady=5)

def abrir_ventana2():
    ventana2 = Toplevel()
    ventana2.title("Ventana 2")
    ventana2.geometry("300x150")
    tk.Label(ventana2, text="Programado con Python", font=("Arial", 12, "bold")).pack(expand=True)


ventana_principal = tk.Tk()
ventana_principal.title("Programa con dos botones")
ventana_principal.geometry("300x200")


btn1 = tk.Button(ventana_principal, text="Mostrar Nombre y Apellido", command=abrir_ventana1)
btn1.pack(pady=20)

btn2 = tk.Button(ventana_principal, text="Mostrar Mensaje", command=abrir_ventana2)
btn2.pack(pady=10)

ventana_principal.mainloop()
