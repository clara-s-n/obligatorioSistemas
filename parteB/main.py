import functions as f
import identification as i
import sys

# Chequear si el usuario está autorizado
if i.is_authorized():
    print("¡Bienvenido!")
else:
    print("Usuario no autorizado. Saliendo del programa.")
    sys.exit()


def main():
    print("Sistema de Gestión de Procesos")
    print("1. Listar Usuarios")
    print("2. Consultar Procesos")
    print("3. Realizar respaldo")
    print("4. Salir")

    while True:
        option = input("Elige una opción: ")

        if option == "1":
            f.list_users()
        elif option == "2":
            f.consult_processes()
        elif option == "3":
            f.doBackup()
        elif option == "4":
            print("Adiós!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
            
if __name__ == "__main__":
    main()