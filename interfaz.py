import os
import subprocess
import tkinter as tk
from datetime import datetime
from tkinter import ttk

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestor de procesos y respaldo")

        self.users = []

        # Obtener usuarios registrados en el sistema operativo
        for user in os.listdir("C:\\Users"):
            if os.path.isdir(os.path.join("C:\\Users", user)):
                self.users.append(user)

        self.menu = tk.Frame(self.root)
        self.menu.pack()

        self.label_username = tk.Label(self.menu, text="Seleccione un usuario:")
        self.label_username.pack(side=tk.LEFT)

        self.combobox_username = ttk.Combobox(self.menu, values=self.users)
        self.combobox_username.pack(side=tk.LEFT)

        self.button_listar_usuario = tk.Button(self.menu, text="Listar usuarios", command=self.listar_usuarios)
        self.button_listar_usuario.pack(side=tk.LEFT)

        self.button_consultar_procesos = tk.Button(self.menu, text="Consultar procesos", command=self.consultar_procesos)
        self.button_consultar_procesos.pack(side=tk.LEFT)

        self.button_realizar_respaldo = tk.Button(self.menu, text="Realizar respaldo", command=self.realizar_respaldo)
        self.button_realizar_respaldo.pack(side=tk.LEFT)

        self.button_salir = tk.Button(self.menu, text="Salir", command=self.salir)
        self.button_salir.pack(side=tk.LEFT)

    def listar_usuarios(self):
        # Mostrar lista de usuarios registrados en el sistema operativo
        # con fecha de ultimo acceso y si tiene respaldo realizado o no
        # ...
        
        # Interfaz gráfica
        self.root.withdraw()
        self.listar_usuarios_window = tk.Toplevel(self.root)
        self.listar_usuarios_window.title("Usuarios registrados")
        
        self.treeview = ttk.Treeview(self.listar_usuarios_window, columns=("last_access", "has_backup"))
        self.treeview.heading("#0", text="Usuario")
        self.treeview.heading("last_access", text="Último acceso")
        self.treeview.heading("has_backup", text="Respaldo")
        self.treeview.pack()
        
        # Lógica
        for user in self.users:
            last_access = datetime.fromtimestamp(os.path.getatime(os.path.join("C:\\Users", user)))
            has_backup = os.path.exists(os.path.join("C:\\Users", user, "backup.zip"))
            
            self.treeview.insert("", "end", text=user, values=(last_access, "Sí" if has_backup else "No"))
            
        # Al cerrar, cerrar la ventana de listar usuarios y mostrar la ventana principal
        self.listar_usuarios_window.protocol("WM_DELETE_WINDOW", self.listar_usuarios_window.destroy) # Cerrar ventana
        self.listar_usuarios_window.protocol("WM_DELETE_WINDOW", self.root.deiconify) # Mostrar ventana principal
        
            

            

    def consultar_procesos(self):
        # Mostrar lista de procesos del usuario seleccionado
        # permitiendo eliminar o pausar a cualquiera de los procesos listados
        # ...
        pass

    def realizar_respaldo(self):
        # Mostrar lista de usuarios que no posean ningún respaldo
        # permitir seleccionar uno y ejecutar el script de respaldo correspondiente
        # ...
        pass

    def salir(self):
        # Emitir mensaje de finalización y cerrar la aplicación
        print("Adiós!")
        self.root.destroy()

if __name__ == "__main__":
    app = Application()
    app.root.mainloop()