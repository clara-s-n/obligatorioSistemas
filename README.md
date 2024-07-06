# Trabajo obligatorio final del grupo 03

**Materia:** Sistemas Operativos

**Fecha:** Julio de 2024

## Integrantes:

- Nicolás Gómez
- Ana Clara Sena
- Juan Tanca

## Defensa: 
[Presentación utilizada](https://www.canva.com/design/DAGJ71djdUo/MJ06vZfpUI11UZI6A-FI-g/view?utm_content=DAGJ71djdUo&utm_campaign=designshare&utm_medium=link&utm_source=editor)

---
A partir de la consigna asignada, elaboramos soluciones según lo que se solicitaba siguiendo los conocimientos aprendidos en clase durante todo este semestre.  

# Parte A:
En primer lugar, se nos pedía crear distintos usuarios, cada uno de estos con especificaciones de seguridad distintas. Para cumplir esta consigna creamos distintos archivos en Powershell ISE de Windows.

Este primer archivo tiene la tarea de, al ejecutarse, crear los distintos usuarios con sus nombres correspondientes: “Contaduría”, “Soporte”, también tenemos otros dos archivos encargados de la creación de los usuarios “Relaciones Públicas”, y “Recepción”, estos tres scripts son los primeros que deben ejecutarse. Todos estos usuarios quedarían validados una vez creados, pero para continuar con la consigna era necesario tener acceso a la dirección de los directorios de cada uno de los usuarios, por lo que es necesario reiniciar la computadora una vez ejecutado el primer script para que se formen automáticamente las carpetas y escritorios de cada usuario y que de esta manera puedan ser accesibles.  

![Captura de pantalla](/parteA.1-2/resultadoCrearUsuarios.png)

![Captura de pantalla](/parteA.3/resultadoScriptUsuario.png)

![Captura de pantalla](/parteA.4/resultadoScriptUsuario.png)

Una vez creados los usuarios y las carpetas de cada uno de estos, creamos otro script, o archivo .ps1 para el siguiente paso, el cual pedía crear ciertas carpetas dentro del escritorio del usuario “Contaduría”. También era necesario crear una carpeta en el directorio raíz, donde se guardarían los respaldos de los usuarios.

Como se ve en el archivo "configuracionUsuarios.ps1", en la carpeta parteA.1-2, el programa verifica dentro del escritorio del usuario contaduría, si la carpeta “Asientos” existe, creándola si ese no es el caso. El proceso se repite para las otras dos carpetas dentro de esta.

![Captura de pantalla](/parteA.1-2/resultadoConfiguracionDeUsuarios.png)

## Creación de la Carpeta "Comunicados":

Primero, verificamos si la carpeta "Comunicados" existía en el Escritorio del usuario. Si no existía, la creamos.
Dentro de la carpeta "Comunicados", creamos dos subcarpetas adicionales llamadas "Semanal" y "Mensual".

## Respaldo de la Carpeta "Comunicados":

Realizamos una copia de la carpeta "Comunicados" y su contenido.
La copia se guardó en una nueva carpeta llamada "Respaldo", ubicada en la raíz del disco principal del equipo.
Dentro de la carpeta "Respaldo", creamos una subcarpeta con el nombre de la fecha en que se realizó el respaldo (por ejemplo, 29FEB2024).
La copia de la carpeta "Comunicados" se guardó dentro de esta subcarpeta con la fecha.

![Captura de pantalla](/parteA.3/resultadoScriptGestionYRespaldo.png)

## Creación del Script de Procesos:

Se define la ruta y el nombre del script PowerShell: C:\Scripts\MonitorProcesos.ps1.
Se verifica si el directorio C:\Scripts existe. Si no, se crea.

Creación de la Carpeta PROCESOS:

Si la carpeta C:\PROCESOS no existe, se crea.

Obtención de los Procesos que Más CPU Consumen:

Se listan los 10 procesos que más CPU consumen, ordenados de mayor a menor.

Registro del Listado de Procesos:

Se genera una marca de tiempo (\$timeStamp) y se crea el contenido del log (\$logContent).
Se añade el contenido del log al archivo especificado (\$logFilePath).

Mostrar el Listado en Pantalla:

Si el usuario logueado es SOPORTE, el listado se muestra en pantalla usando Write-Host.

## Configuración de la Tarea Programada:

Verificación y Eliminación de la Tarea Programada Existente:

Si una tarea programada con el nombre MonitorarProcesosCPU ya existe, se elimina.

Definición de la Acción de la Tarea Programada:

La acción consiste en ejecutar el script PowerShell MonitorProcesos.ps1 utilizando powershell.exe.

Definición de los Triggers de la Tarea Programada:

triggerStartup: Ejecutar la tarea al inicio del sistema operativo.

triggerRepetition: Ejecutar la tarea cada 60 minutos, durante 10 años (RepetitionDuration de 3650 días).

![Captura de pantalla](/parteA.5/resultadoScript2.png)

---
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
net localgroup ParteA Contaduria /add
net localgroup ParteA Soporte /add
net localgroup ParteA Recepcion /add
net localgroup ParteA RelacionesPublicas /add
```
![Alt text](/parteB/images/grupoLocal.png)

2. **Configurar el script para autenticar usuarios**: Modificamos el script para que verifique si el usuario actual pertenece al grupo "ParteA" antes de permitir que ejecute el script.

Utilizamos la biblioteca `getpass` para obtener el nombre de usuario actual y luego verificar si pertenece al grupo "ParteA" utilizando la biblioteca `win32net`.

### Imagenes del menú:

Menú no disponible:

![](/parteB/images/noDisponible.png)

**Disclaimer: para las siguientes imagenes le sacamos el chequeo al principio del archivo "main.py" que se encuentra en la carpeta "parteB"**

1. Listar usuarios:

![listarUsuarios.png](/parteB/images/listarUsuarios.png)

2. Consultar procesos:

![consultarProcesos.png](/parteB/images/consultarProcesos.png)

 - Datos de un proceso y opciones (eliminar o pausar): 

  ![consultarProcesos2.png](/parteB/images/consultarProcesos2.png)

3. Backup no permitido (porque el usuario no es uno de los permitidos):

![backupNoPermitido.png](/parteB/images/backupNoPermitido.png)
