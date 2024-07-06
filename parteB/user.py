class User:
    def __init__(self, name, group, last_access, has_backup):
        self.name = name
        self.group = group
        self.last_access = last_access
        self.has_backup = has_backup

    def __str__(self):
        return f"Nombre: {self.name}, Grupo: {self.group}, Fecha de último acceso: {self.last_access}, Respaldo: {'SI' if self.has_backup else 'NO'}"