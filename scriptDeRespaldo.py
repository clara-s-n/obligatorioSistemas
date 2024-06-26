import os
from datetime import datetime
import subprocess

def backup_user(username):
    # Crear carpeta de respaldo si no existe
    backup_dir = "C:\\Respaldo"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Crear carpeta de respaldo para el usuario
    user_backup_dir = os.path.join(backup_dir, f"{username}_{datetime.date.today()}.zip")
    if not os.path.exists(user_backup_dir):
        subprocess.run(["robocopy", "/e", "/minlatency", f"C:\\Users\\{username}\\", user_backup_dir])
        
# A este habría que cambiarlo cuando tenga el script de la parte A