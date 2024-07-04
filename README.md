# obligatorioSistemas


# Parte B:
Versión de python: 3.12.4
Verión de vscode: 1.90.2
Hay que hacer un install de las librerías psutil y pywin32, utilizando los siguientes comandos

+ PSutil
```
pip install psutil
```

+ pywin32
```
pip install pywin32
```

## Justificación

**Clase User**

La clase `User` es un objeto que representa a un usuario del sistema. Tiene cuatro atributos: `name` (nombre del usuario), `group` (grupo al que pertenece el usuario), `last_access` (fecha de último acceso del usuario) y `has_backup` (si el usuario tiene o no tiene un respaldo).

La función `__str__` se utiliza para representar el objeto `User` como una cadena, lo que es útil para mostrar la información del usuario en la terminal.

**Función get_users**

La función `get_users` se encarga de obtener la lista de usuarios del sistema utilizando la biblioteca `win32net`. La función itera sobre la lista de usuarios y crea objetos `User` para cada uno de ellos. Luego, devuelve la lista de objetos `User`.

**Main**

La función `main` es el punto de entrada del programa. Inicializa el menú principal y llama a las funciones según la opción seleccionada por el usuario.

**Opciones**

La función `list_users` muestra la lista de usuarios del sistema y permite al usuario elegir una opción para mostrar más información sobre los usuarios o regresar al menú principal.

La función `consult_procesos` muestra la lista de procesos actuales y permite al usuario elegir un proceso para mostrar más información o regresar al menú principal.

La función `realizar_respaldo` muestra la lista de usuarios que no tienen respaldo y permite al usuario elegir uno para realizar el respaldo.

**Por qué es buena idea hacerlo así**

1. **Organización**: La estructura del código es clara y fácil de entender, con funciones bien definidas y nombres descriptivos.
2. **Reutilización**: Las funciones pueden ser reutilizadas en diferentes partes del código, lo que reduce la duplicación de código y facilita la mantenibilidad.
3. **Flexibilidad**: El uso de objetos `User` permite fácilmente agregar o eliminar atributos o métodos según sea necesario.
4. **Seguridad**: La función `get_users` utiliza la biblioteca `win32net` para obtener la lista de usuarios, lo que reduce el riesgo de seguridad al no tener que preocuparse por acceder directamente a la información del sistema operativo.
5. **Portabilidad**: El uso de bibliotecas como `psutil` y `datetime` hace que el código sea portable entre diferentes sistemas operativos.
6. **Legibilidad**: El código es fácil de leer y entender, lo que facilita la mantenibilidad y el debugging.

## Configuración de permisos
**Requisito:**

1. Los usuarios creados en la Parte A deben tener un grupo específico, en este caso, "ParteA".
2. El script debe estar configurado para que solo los usuarios del grupo "ParteA" puedan ejecutarlo.

**Solución:**

1. **Crear el grupo "ParteA"**: Utilizando el comando `net localgroup` para crear un grupo llamado "ParteA" y agregar a los usuarios que desees.
```bash
net localgroup ParteA /add
net localgroup ParteA Contaduria Soporte Recepcion RelacionesPublicas
```


2. **Configurar el script para autenticar usuarios**: Modificamos el script para que verifique si el usuario actual pertenece al grupo "ParteA" antes de permitir que ejecute el script.

Utilizamos la biblioteca `getpass` para obtener el nombre de usuario actual y luego verificar si pertenece al grupo "ParteA" utilizando la biblioteca `win32security`.