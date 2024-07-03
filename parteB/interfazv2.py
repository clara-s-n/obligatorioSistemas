import datetime
import os
import win32net
import win32netcon
import parteB.scriptDeRespaldo as scriptDeRespaldo
import psutil
import tkinter as tk
from tkinter import messagebox, simpledialog

class User:
    def __init__(self, name, group, last_access, has_backup):
        self.name = name
        self.group = group
        self.last_access = last_access
        self.has_backup = has_backup

    def __str__(self):
        return f"Nombre: {self.name}, Grupo: {self.group}, Fecha de último acceso: {self.last_access}, Respaldo: {'SI' if self.has_backup else 'NO'}"

# Obtenemos la lista de usuarios del sistema
users = []

def get_users():
    users = []
    resume = 0
    while True:
        user_list, total, resume = win32net.NetUserEnum(None, 0, win32netcon.FILTER_NORMAL_ACCOUNT, resume)
        for user_info in user_list:
            user_name = user_info['name']
            try:
                group = win32net.NetUserGetGroups(None, user_name)[0][0]
            except IndexError:
                group = "Unknown"
            
            user_info_2 = win32net.NetUserGetInfo(None, user_name, 2)
            last_logon_timestamp = user_info_2['last_logon']
            last_access = datetime.datetime.fromtimestamp(last_logon_timestamp).strftime("%Y-%m-%d %H:%M:%S")
            
            backup_path = os.path.join('C:\\Respaldo', user_name)
            has_backup = os.path.exists(backup_path)
            user = User(user_name, group, last_access, has_backup)
            users.append(user)
        if not resume:
            break
    return users

def list_users():
    global users
    users = get_users()
    if not users:
        messagebox.showinfo("Información", "No se encontraron usuarios")
        return
    
    user_info = "\n".join(str(user) for user in users)
    messagebox.showinfo("Lista de usuarios", user_info)
    mostrar_menu()

def consult_procesos():
    process_info = []
    for process in psutil.process_iter():
        try:
            process_name = process.name()
            process_id = process.pid
            cpu_times = process.cpu_times()
            process_status = process.status()
            process_info.append(f"Nombre: {process_name}, ID: {process_id}, Tiempo de CPU usuario: {cpu_times.user}, Tiempo de CPU sistema: {cpu_times.system}, Estado: {process_status}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    process_info_str = "\n".join(process_info)
    messagebox.showinfo("Lista de procesos", process_info_str)
    
    option = simpledialog.askstring("Opciones", "1. Consultar proceso\n2. Volver al menú principal\nElige una opción:")
    if option == "1":
        consultar_proceso()
    elif option == "2":
        mostrar_menu()
    else:
        messagebox.showinfo("Error", "Opción no válida")

def consultar_proceso():
    process_id = simpledialog.askstring("Consulta de proceso", "Ingresa el ID del proceso:")
    process = next((p for p in psutil.process_iter() if p.pid == int(process_id)), None)
    
    if process:
        process_details = (f"Nombre: {process.name()}\n"
                           f"ID: {process.pid}\n"
                           f"Tiempo de ejecución: {datetime.datetime.now() - datetime.datetime.fromtimestamp(process.create_time())}\n"
                           f"Usuario: {process.username()}\n"
                           f"Estado: {'Activo' if process.is_running() else 'Inactivo'}")
        
        option = simpledialog.askstring("Opciones", f"{process_details}\n\n1. Finalizar proceso\n2. Pausar proceso\n3. Volver al menú principal\nElige una opción:")
        if option == "1":
            process.terminate()
            messagebox.showinfo("Información", "Proceso finalizado")
        elif option == "2":
            process.suspend()
            messagebox.showinfo("Información", "Proceso pausado")
        elif option == "3":
            mostrar_menu()
            return
        else:
            messagebox.showinfo("Error", "Opción no válida")
    else:
        messagebox.showinfo("Error", "Proceso no encontrado")
    mostrar_menu()

def realizar_respaldo():
    global users
    users = get_users()
    if not users:
        messagebox.showinfo("Información", "No se encontraron usuarios")
        return
    
    users_without_backup = [str(user) for user in users if not user.has_backup]
    if users_without_backup:
        user_info = "\n".join(users_without_backup)
        user_name = simpledialog.askstring("Usuarios sin respaldo", f"{user_info}\n\nIngresa el nombre del usuario que deseas respaldar:")
        user = next((user for user in users if user.name == user_name), None)
        if user:
            if user.has_backup:
                messagebox.showinfo("Información", "El usuario ya tiene respaldo")
            else:
                scriptDeRespaldo.backup_user(user_name)
                messagebox.showinfo("Información", f"Respaldo realizado para el usuario {user_name}")
        else:
            messagebox.showinfo("Error", "Usuario no encontrado")
    else:
        messagebox.showinfo("Información", "No hay usuarios sin respaldo")
    mostrar_menu()

def mostrar_menu():
    option = simpledialog.askstring("Menú principal", "Sistema de Gestión de Procesos\n\n1. Listar Usuarios\n2. Consultar Procesos\n3. Realizar respaldo\n4. Salir\n\nElige una opción:")
    if option == "1":
        list_users()
    elif option == "2":
        consult_procesos()
    elif option == "3":
        realizar_respaldo()
    elif option == "4":
        root.destroy()
    else:
        messagebox.showinfo("Error", "Opción no válida")
        mostrar_menu()

def main():
    global root
    root = tk.Tk()
    root.withdraw()
    mostrar_menu()
    root.mainloop()

if __name__ == "__main__":
    main()
