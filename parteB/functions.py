import os
import datetime
import win32net
import win32netcon
from user import User
import psutil
import backup

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

# Función para mostrar el menú
def showMenu():
    print("\nSistema de Gestión de Procesos")
    print("1. Listar Usuarios")
    print("2. Consultar Procesos")
    print("3. Realizar respaldo")
    print("4. Salir")
    return

# Función para mostrar la lista de usuarios
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
    
    # Mostrar opciones
    input("Presiona Enter para continuar...")
    showMenu()

# Función para consultar procesos
def consult_processes():
    # Listar procesos
    print("Lista de procesos:")
    for process in psutil.process_iter():
        try:
            process_name = process.name()
            process_id = process.pid
            # Mostrar el consumo de CPU y estado del proceso
            cpu_times = process.cpu_times()
            process_status = process.status()
            print(f"Nombre: {process_name}, ID: {process_id}, Tiempo de CPU usuario: {cpu_times.user}, Tiempo de CPU sistema: {cpu_times.system} Estado: {process_status}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): # Ignorar errores
            pass
    
    # Desplegar opciones
    print("1. Consultar proceso")
    print("2. Volver al menú principal")
    option = input("Elige una opción: ")
    if option == "1":
        process_options()
    elif option == "2":
        showMenu()
    else:
        print("Opción no válida")
        

# Función para procesar opciones de un proceso (finalizar, pausar)
def process_options():
    # Consultar proceso
    process_id = input("Ingresa el ID del proceso: ")
    process = next((process for process in psutil.process_iter() if process.pid == int(process_id)), None)
    
    if process:
        print("Información del proceso:")
        print(f"Nombre: {process.name()}")
        print(f"ID: {process.pid}")
        print(f"Tiempo de ejecución: {datetime.datetime.now() - datetime.datetime.fromtimestamp(process.create_time())}")
        print(f"Usuario: {process.username()}")
        print(f"Estado: {'Activo' if process.is_running() else 'Inactivo'}")
        
        # Mostrar opciones
        print("1. Finalizar proceso")
        print("2. Pausar proceso")
        print("3. Volver al menú principal")
        option = input("Elige una opción: ")
        if option == "1":
            process.terminate()
            print("Proceso finalizado")
        elif option == "2":
            process.suspend()
            print("Proceso pausado")
        elif option == "3":
            showMenu()
            return
        else:
            print("Opción no válida")
            
    else:
        print("Proceso no encontrado")
        

# Función para realizar respaldo
def doBackup():
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
            backup.backup_user(user_name)
    else:
        print("Usuario no encontrado")
    
    # Mostrar opciones
    input("Presiona Enter para continuar...")
    showMenu()
