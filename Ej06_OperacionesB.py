 # CBTIS 89
# Elizabeth Lara Acuña 
# 3°B Programa T.M
# programa que tenga varias operaciones 
import tkinter as tk

def sumar():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      suma = num1 + num2
      resultado.config(text=f"Resultado: {suma}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
def restar():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      restar = num1 - num2
      resultado.config(text=f"Resultado: {restar}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
      
def mul():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      mul = num1 * num2
      resultado.config(text=f"Resultado: {mul}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
def div():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      div = num1 /num2
      resultado.config(text=f"Resultado: {div}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")

# Crear la ventana principal
ventana= tk.Tk()
ventana.title("operaciones de dos números")
ventana.geometry("350x230")
# Crear los cuadros de texto
entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)
# Posicionar las entradas en la ventana
entrada1.pack(pady=5)
entrada2.pack(pady=5)

# Crear botón de suma
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)

boton_restar= tk.Button(ventana, text="restar", command=restar)
boton_restar.pack(pady=5)
boton_mul= tk.Button(ventana, text="multiplicar", command=mul)
boton_mul.pack(pady=5)
boton_div= tk.Button(ventana, text="dividir", command=div)
boton_div.pack(pady=5)

# Crear etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)


# Ejecutar la aplicación
ventana.mainloop()