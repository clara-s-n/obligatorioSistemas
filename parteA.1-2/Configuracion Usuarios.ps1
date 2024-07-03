$contaduriaPathDesk = "C:\Users\Contaduria\Desktop" # Path del escritorio de Contaduria

$contaduriaUser = "Contaduria" # Usuario de Contaduria

$rutaRespaldo = "C:\Respaldo\$contaduriaUser" # Path de la carpeta de respaldo

$pathAsientos = Join-Path $contaduriaPathDesk -ChildPath "Asientos" # Path de la carpeta 'Asientos'

$interiorAsientos = @("Diario", "Semanal") # Carpetas dentro de 'Asientos'

foreach ($user in $allUsers) {
    # Se recorren todos los usuarios
    $userFolder = "$usersFolder\$user\Desktop" # Se obtiene el path del escritorio del usuario
    if (Test-Path -Path $userFolder) {
        # Se verifica si el usuario tiene escritorio
        $acl = Get-Acl -Path $userFolder # Se obtiene el ACL del escritorio
        $denyRule = New-Object System.Security.AccessControl.FileSystemAccessRule($contaduriaUser, "FullControl", "ContainerInherit, ObjectInherit", "None", "Deny") # Se crea una regla de acceso para denegar el acceso a Contaduria
        $acl.AddAccessRule($denyRule) # Se añade la regla al ACL
        Set-Acl -Path $userFolder -AclObject $acl # Se actualiza el ACL del escritorio
    }
}


if (!(Test-Path -Path $pathAsientos -PathType Container)) {
    # Se verifica si la carpeta 'Asientos' existe
    New-Item -Path $pathAsientos -ItemType Directory # Se crea la carpeta 'Asientos'
    Write-Output "La carpeta 'Asientos' no existía y se ha creado." # Se muestra un mensaje
}
else { 
    Write-Output "La carpeta 'Asientos' ya existe." 
}

foreach ($carpeta in $interiorAsientos) {
    # Se recorren las carpetas dentro de 'Asientos'
    $pathInteriorAsientos = Join-Path $pathAsientos -ChildPath $carpeta # Se obtiene el path de la carpeta
    if (!(Test-Path -Path $pathInteriorAsientos -PathType Container)) {
        # Se verifica si la carpeta existe
        New-Item -Path $pathInteriorAsientos -ItemType Directory # Se crea la carpeta
        Write-Output "La carpeta '$carpeta' no existía y se ha creado." # Se muestra un mensaje
    }
    else {
        Write-Output "La carpeta '$carpeta' ya existe."
    }
}

$fecha = Get-Date -Format "ddMMMyyyy" # Se obtiene la fecha actual en formato ddMMMyyyy
$respaldoCarpeta = "$rutaRespaldo\$fecha" # Se obtiene el path de la carpeta de respaldo
$contaduriaProfile = "C:\Users\Contaduria" # Path del perfil de Contaduria

if (!(Test-Path -Path $respaldoCarpeta)) {
    # Se verifica si la carpeta de respaldo existe
    New-Item -ItemType Directory -Path $respaldoCarpeta # Se crea la carpeta de respaldo
    Copy-Item -Path $contaduriaProfile -Destination $respaldoCarpeta -Recurse # Se copia el perfil de Contaduria a la carpeta de respaldo
}

$acl = Get-Acl -Path $contaduriaProfile # Se obtiene el ACL del perfil de Contaduria

$accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule($contaduriaUser, "Read, Write", "ContainerInherit, ObjectInherit", "None", "Allow") # Se crea una regla de acceso para permitir el acceso a Contaduria
$acl.SetAccessRule($accessRule) # Se añade la regla al ACL
Set-Acl -Path $contaduriaProfile -AclObject $acl # Se actualiza el ACL del perfil de Contaduria
$usersFolder = "C:\Users" # Path de la carpeta de usuarios
$allUsers = Get-ChildItem -Path $usersFolder | Where-Object { $_.Name -ne $contaduriaUser } # Se obtienen todos los usuarios excepto Contaduria

foreach ($user in $allUsers) {
    # Se recorren todos los usuarios
    $userFolder = "$usersFolder\$user\Desktop" # Se obtiene el path del escritorio del usuario
    if (Test-Path -Path $userFolder) {
        # Se verifica si el usuario tiene escritorio
        $acl = Get-Acl -Path $userFolder # Se obtiene el ACL del escritorio
        $denyRule = New-Object System.Security.AccessControl.FileSystemAccessRule($contaduriaUser, "FullControl", "ContainerInherit, ObjectInherit", "None", "Deny") # Se crea una regla de acceso para denegar el acceso a Contaduria
        $acl.AddAccessRule($denyRule) # Se añade la regla al ACL
        Set-Acl -Path $userFolder -AclObject $acl # Se actualiza el ACL del escritorio
    }
}


$usuarioSoporte = "Soporte" # Usuario de Soporte
$supportFolders = Get-ChildItem -Path $usersFolder # Se obtienen todas las carpetas de usuarios

foreach ($folder in $supportFolders) {
    # Se recorren todas las carpetas de usuarios
    $folderPath = $folder.FullName # Se obtiene el path de la carpeta
    $acl = Get-Acl -Path $folderPath # Se obtiene el ACL de la carpeta
    $accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule($usuarioSoporte, "FullControl", "ContainerInherit, ObjectInherit", "None", "Allow")
    $acl.SetAccessRule($accessRule) # Se añade la regla al ACL
    Set-Acl -Path $folderPath -AclObject $acl # Se actualiza el ACL de la carpeta
}
