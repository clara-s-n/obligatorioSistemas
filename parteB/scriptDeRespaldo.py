import os
from datetime import datetime
import subprocess

def backup_user(username):
    # Crear carpeta de respaldo si no existe
    backup_dir = f"C:\\Respaldo\\{username}"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Crear carpeta de respaldo para el usuario
    # Si el usuario es "Contaduria", se copia solamente la carpeta Asientos y las subcarpetas
    # Si el usuario es "Relaciones Publicas", se copia solamente la carpeta Comunicados y las subcarpetas
    
    if username == "Contaduria":
        source_dir = "C:\\Users\\Contaduria\\Desktop\\Asientos"
    elif username == "RelacionesPublicas":
        source_dir = "C:\\Users\\Relaciones Publicas\\Desktop\\Comunicados"
    else:
        print("Usuario no válido")
        return
    
    # Copiar carpeta de respaldo, ponerle la fecha y comprimir
    backup_path = os.path.join(backup_dir, f"{username}_{datetime.now().strftime('%Y%m%d%H%M%S')}.zip")
    subprocess.run(["powershell", "Compress-Archive", source_dir, backup_path])
        
    print(f"Respaldo realizado para el usuario {username}")
# A este habría que cambiarlo cuando tenga el script de la parte A