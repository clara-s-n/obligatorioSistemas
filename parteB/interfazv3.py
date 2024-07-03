import tkinter as tk
from tkinter import messagebox
import datetime
import os
import win32net
import win32netcon
import psutil
import parteB.scriptDeRespaldo as scriptDeRespaldo


class User:
    def __init__(self, name, group, last_access, has_backup):
        self.name = name
        self.group = group
        self.last_access = last_access
        self.has_backup = has_backup

    def __str__(self):
        return f"Nombre: {self.name}, Grupo: {self.group}, Fecha de último acceso: {self.last_access}, Respaldo: {'SI' if self.has_backup else 'NO'}"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack()

        self.list_users_button = tk.Button(self.menu_frame, text="Listar usuarios", command=self.list_users)
        self.list_users_button.pack(side="left")

        self.consult_procesos_button = tk.Button(self.menu_frame, text="Consultar procesos", command=self.consult_procesos)
        self.consult_procesos_button.pack(side="left")

        self.realizar_respaldo_button = tk.Button(self.menu_frame, text="Realizar respaldo", command=self.realizar_respaldo)
        self.realizar_respaldo_button.pack(side="left")

        self.salir_button = tk.Button(self.menu_frame, text="Salir", command=self.master.destroy)
        self.salir_button.pack(side="left")
        
        
    def get_users(self):
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
        
    def list_users(self):
        users = self.get_users()
        if not users:
            messagebox.showinfo("Error", "No se encontraron usuarios")
            return

        list_text = "Lista de usuarios:\n"
        for user in users:
            list_text += str(user) + "\n"
        messagebox.showinfo("Usuarios", list_text)

    def consult_procesos(self):
        # Listar procesos
        process_list_text = "Lista de procesos:\n"
        for process in psutil.process_iter():
            try:
                process_name = process.name()
                process_id = process.pid
                cpu_times = process.cpu_times()
                process_status = process.status()
                process_list_text += f"Nombre: {process_name}, ID: {process_id}, Tiempo de CPU usuario: {cpu_times.user}, Tiempo de CPU sistema: {cpu_times.system} Estado: {process_status}\n"
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): # Ignorar errores
                pass
        
        messagebox.showinfo("Procesos", process_list_text)

    def realizar_respaldo(self):
        users = self.get_users()
        if not users:
            messagebox.showinfo("Error", "No se encontraron usuarios")
            return

        user_list_text = "Usuarios sin respaldo:\n"
        for user in users:
            if not user.has_backup:
                user_list_text += str(user) + "\n"
        
        result = messagebox.askokcancel("Respaldo", user_list_text)
        if result:
            scriptDeRespaldo.backup_user(input("Ingresa el nombre del usuario: "))
            messagebox.showinfo("Respaldo", "Respaldo realizado con éxito")

root = tk.Tk()
app = Application(master=root)
app.mainloop()