import getpass
import win32net

def is_authorized():
    # Obtener el nombre de usuario actual
    user_name = getpass.getuser()

    # Obtener los grupos a los que pertenece el usuario
    user_info = win32net.NetUserGetLocalGroups(None, user_name)

    # Verificar si el usuario pertenece al grupo "ParteA"
    if 'ParteA' in user_info:
        return True
    else:
        return False
