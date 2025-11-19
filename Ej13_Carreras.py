#CBTIS 89
#3°B PROGRAMACION MATUTINO 
#CESAR ARMANDO MARTINEZ COVARRUBIAS
#Programa que muestra una  ventana con una etiqueta y un boton

import tkinter as tk 
from tkinter import ttk 

ventana=tk.Tk()
ventana.title("lista de desplegue ComboBox")
ventana.geometry("300x200")

etiqueta= tk.Label(ventana,text="elije una opcion")
etiqueta.pack(pady=10)

opciones = ["ARH","Arquitectura","Comercio electronico","Comercio internacional y aduanas",
"Construccion","Contabilidad","Mecatronica","Programacion"]
ComboColores = ttk.Combobox(ventana,values=opciones,state="readonly")
ComboColores.pack(pady=5)

def mostrar_seleccion(event):
    seleccion =  ComboColores.get()
    etiqueta_resultado.config(text=f"Seleccionaste:{seleccion}")

ComboColores.bind("<<ComboboxSelected>>",mostrar_seleccion)

etiqueta_resultado=tk.Label(ventana,text="Aun no has seleccionado nada")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()