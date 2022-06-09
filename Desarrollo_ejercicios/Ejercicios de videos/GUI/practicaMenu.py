from tkinter import *
from tkinter import messagebox

root=Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Jorge", "Procesador de textos 2022.")

def avisoLicencia():
    messagebox.showwarning("Licencia","Producto con licencia caducada.")
    
def salirAplicacion():
    #valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?") # Entrega de vuelta los valores: si o no.
    valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?") # Entrega de vuelta los valores booleanos True o False
    if valor:
        root.destroy()
        
def cerrardocumento():
    valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado.")
    if valor:
        root.destroy()           

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrardocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

edicionMenu=Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")

herramientasMenu=Menu(barraMenu, tearoff=0)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=edicionMenu)
barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

root.mainloop()