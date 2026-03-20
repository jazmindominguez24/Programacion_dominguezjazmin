import tkinter as tk
from tkinter import messagebox

# FUNCIONES 

def agregar_helado():
    tipo = ventana.tipo_var.get()
    seleccion = lista_sabores.curselection()
    pedido = [lista_sabores.get(i) for i in seleccion]
    # SI ES POR BOCHAS
    if tipo == "bocha":
        bochas = ventana.bochas_var.get()

        if len(pedido) != bochas:
            messagebox.showwarning("Error", f"Debe elegir exactamente {bochas} sabores.")
            return

        if bochas == 1:
            precio = 700
        elif bochas == 2:
            precio = 1200
        else:
            precio = 1600
    # SI ES POR KILO
    else:
        if len(pedido) == 0:
            messagebox.showwarning("Error", "Debe elegir al menos un sabor.")
            return

        if tipo == "cuarto":
            precio = 3500
        elif tipo == "medio":
            precio = 7000
        elif tipo == "kilo":
            precio = 14000

    # GUARDAR
    ventana.factura.append((ventana.numero_helado, pedido, precio))
    ventana.total += precio
    ventana.numero_helado += 1

    messagebox.showinfo("Agregado", "Pedido agregado correctamente.")#MENSAJE DE QUE SE AGREGO

    lista_sabores.selection_clear(0, tk.END)#LIMPIA LA SELECCION
    ventana.bochas_var.set(1)
    actualizar_lista_pedido()
def eliminar_helado():
    seleccion = lista_pedido.curselection()
    
    if not seleccion:
        messagebox.showwarning("Error", "Seleccione un helado para eliminar.")
        return

    indice = seleccion[0]
    
    # RESTAR DEL TOTAL
    ventana.total -= ventana.factura[indice][2]
    
    # se elinina de la lista
    ventana.factura.pop(indice)

    # Actualizar numeración
    for i in range(len(ventana.factura)):
        ventana.factura[i] = (i+1, ventana.factura[i][1], ventana.factura[i][2])

    ventana.numero_helado = len(ventana.factura) + 1

    actualizar_lista_pedido()
def actualizar_lista_pedido():
    lista_pedido.delete(0, tk.END)
    for helado in ventana.factura:
        texto = f"Helado {helado[0]} - {', '.join(helado[1])} - ${helado[2]}"
        lista_pedido.insert(tk.END, texto)

def terminar_pedido():
    if not ventana.factura:
        messagebox.showwarning("Aviso", "No hay ningún pedido para facturar.")
        return
    actualizar_lista_pedido()

    texto = "FACTURA FINAL\n" + "-"*20 + "\n"
    for helado in ventana.factura:
        texto += f"Helado {helado[0]}\nSabores: {', '.join(helado[1])}\nPrecio: ${helado[2]}\n\n"
    
    texto += "-"*20 + f"\nTotal a pagar: ${ventana.total}"
    
    messagebox.showinfo("Factura", texto)

    # reiniciar variables
    ventana.factura = []
    ventana.total = 0
    ventana.numero_helado = 1
    lista_sabores.selection_clear(0, tk.END)
    ventana.bochas_var.set(1)

def salir_programa():
    if messagebox.askyesno("Salir", "¿Desea cerrar la aplicación?"):
        ventana.destroy()

# INTERFAZ 

ventana = tk.Tk()
ventana.title("Heladería Dulce Frío - Sistema de Ventas")
ventana.geometry("800x550")
ventana.configure(bg="#f2f2f2")

# variables globales 
ventana.factura = []
ventana.total = 0
ventana.numero_helado = 1
ventana.bochas_var = tk.IntVar(value=1)
ventana.tipo_var = tk.StringVar(value="bocha")

# tittulo principal
titulo = tk.Label(ventana, text="Heladería Dulce Frío", font=("Arial", 20, "bold"), 
                  bg="#9b5e8e", fg="white", pady=10)
titulo.pack(fill="x")

# framer principal para columnas
menu_frame = tk.Frame(ventana, bg="#f2f2f2")
menu_frame.pack(expand=True, fill="both", padx=20, pady=20)

# FRAME BOCHAS 
frame_izq = tk.Frame(menu_frame, bg="#c3e3fb", bd=2, relief="groove")
frame_izq.pack(side="left", padx=20, fill="y")

tk.Label(frame_izq, text="Cantidad de Bochas", font=("Arial", 12, "bold"), bg="#c3e3fb").pack(pady=10)

opciones_bochas = [("1 Bocha ($700)", 1), ("2 Bochas ($1200)", 2), ("3 Bochas ($1600)", 3)]
for text, val in opciones_bochas:
    tk.Radiobutton(frame_izq, text=text, variable=ventana.bochas_var, value=val, 
                   bg="#c3e3fb", font=("Arial", 11), anchor="w").pack(fill="x", padx=20, pady=5)
# FRAME bocha o kilo
frame_tipo = tk.Frame(menu_frame, bg="#d1f2eb", bd=2, relief="groove")
frame_tipo.pack(side="left", padx=20, fill="y")

tk.Label(frame_tipo, text="Tipo de Pedido", font=("Arial", 12, "bold"), bg="#d1f2eb").pack(pady=10)

tk.Radiobutton(frame_tipo, text="Por Bochas", variable=ventana.tipo_var, value="bocha",
               bg="#d1f2eb").pack(anchor="w", padx=20)

tk.Radiobutton(frame_tipo, text="1/4 Kg ($3500)", variable=ventana.tipo_var, value="cuarto",
               bg="#d1f2eb").pack(anchor="w", padx=20)

tk.Radiobutton(frame_tipo, text="1/2 Kg ($7000)", variable=ventana.tipo_var, value="medio",
               bg="#d1f2eb").pack(anchor="w", padx=20)

tk.Radiobutton(frame_tipo, text="1 Kg ($14000)", variable=ventana.tipo_var, value="kilo",
               bg="#d1f2eb").pack(anchor="w", padx=20)

# FRAME SABORES 
frame_der = tk.Frame(menu_frame, bg="#bce8f5", bd=2, relief="groove")
frame_der.pack(side="right", padx=20, fill="y")

tk.Label(frame_der, text="Seleccione Sabores", font=("Arial", 12, "bold"), bg="#bce8f5").pack(pady=10)

sabores = ["Chocolate", "Vainilla", "Frutilla", "Dulce de leche", "Limón", 
           "Menta granizada", "Banana split", "Cookies & cream", "Coco", "Maracuyá","Cereza","Chocolate dubai"]

lista_sabores = tk.Listbox(frame_der, selectmode=tk.MULTIPLE, width=30, height=12, 
                           bg="#ffffff", font=("Arial", 10))
lista_sabores.pack(padx=15, pady=10)

for s in sabores:
    lista_sabores.insert(tk.END, s)

# FRAME PEDIDO ACTUAL
frame_pedido = tk.Frame(ventana, bg="#fff3cd", bd=2, relief="groove")
frame_pedido.pack(padx=20, pady=10, fill="x")

tk.Label(frame_pedido, text="Pedido Actual", font=("Arial", 12, "bold"), bg="#fff3cd").pack()

lista_pedido = tk.Listbox(frame_pedido, height=6, font=("Arial", 10))
lista_pedido.pack(padx=10, pady=10, fill="x")

# BOTONES DE ACCIÓN (Abajo) 
frame_botones = tk.Frame(ventana, bg="#f2f2f2")
frame_botones.pack(pady=20)

boton_agregar = tk.Button(frame_botones, text="Agregar Helado", command=agregar_helado, 
                        bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=15)
boton_agregar.grid(row=0, column=0, padx=10)

boton_terminar = tk.Button(frame_botones, text="Terminar Pedido", command=terminar_pedido, 
                         bg="#2196F3", fg="white", font=("Arial", 10, "bold"), width=15)
boton_terminar.grid(row=0, column=1, padx=10)

boton_salir = tk.Button(frame_botones, text="Finalizar Programa", command=salir_programa, 
                      bg="#f44336", fg="white", font=("Arial", 10, "bold"), width=15)
boton_salir.grid(row=0, column=2, padx=10)
boton_eliminar = tk.Button(frame_botones, text="Eliminar Helado", command=eliminar_helado, 
                        bg="#ff9800", fg="white", font=("Arial", 10, "bold"), width=15)
boton_eliminar.grid(row=0, column=3, padx=10)

ventana.mainloop()