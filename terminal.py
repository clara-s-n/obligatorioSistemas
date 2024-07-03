import datetime
import os
import win32net
import win32netcon
import scriptDeRespaldo

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


def main():
    print("Sistema de Gestión de Procesos")
    print("1. Listar Usuarios")
    print("2. Consultar Procesos")
    print("3. Realizar respaldo")
    print("4. Salir")

    while True:
        option = input("Elige una opción: ")

        if option == "1":
            list_users()
        elif option == "2":
            consult_procesos()
        elif option == "3":
            realizar_respaldo()
        elif option == "4":
            print("Adiós!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def list_users():
    global users
    # Obtenemos la lista de usuarios del sistema
    users = get_users()
    if not users:
        print("No se encontraron usuarios")
        return
    print("Lista de usuarios:")
    for user in users:
        print(user)

def consult_procesos():
    """Deberá mostrar una lista de los procesos del Usuario especificado (datos a mostrar ID, 
Nombre, % CPU y Estado) permitiendo eliminar o pausar a cualquiera de los procesos 
listados.
"""
    # Mostrar lista de procesos del usuario logueado
    # permitiendo eliminar o pausar a cualquiera de los procesos listados
    
    # 1. Obtener lista de procesos del usuario logueado
    # 2. Mostrar lista de procesos con ID, Nombre, % CPU y Estado
    # 3. Permitir eliminar o pausar a cualquiera de los procesos listados
    
    

def realizar_respaldo():
    # Mostrar lista de usuarios que no posean ningún respaldo
    global users
    users = get_users()
    if not users:
        print("No se encontraron usuarios")
        return

    print("Usuarios sin respaldo:")
    for user in users:
        if not user.has_backup:
            print(user)
    
    # Seleccionar usuario que no tenga respaldo
    user_name = input("Ingresa el nombre del usuario: ")
    user = next((user for user in users if user.name == user_name), None)
    if user:
        if user.has_backup:
            print("El usuario ya tiene respaldo")
        else:
            # Realizar respaldo
            scriptDeRespaldo.backup_user(user_name)
    else:
        print("Usuario no encontrado")

if __name__ == "__main__":
    main()
