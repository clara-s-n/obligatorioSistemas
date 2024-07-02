$userName = "RelacionesPublicas"
$homeDirectory = "C:\Users\$userName"

$usersDirectory = "C:\Users"
$otherUsers = Get-ChildItem -Path $usersDirectory -Directory | Where-Object { $_.Name -ne $userName }

foreach ($user in $otherUsers) {
    $path = "$usersDirectory\$($user.Name)"
    $acl = Get-Acl -Path $path
    $accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("$userName", "FullControl", "Deny")
    $acl.SetAccessRule($accessRule)
    Set-Acl -Path $path -AclObject $acl
}

# restringimos privilegios de instalación
# añadimos el usuario al grupo "Usuarios Restringidos" (si existe)
if (Get-LocalGroup -Name "Restricted Users" -ErrorAction SilentlyContinue) {
    Add-LocalGroupMember -Group "Restricted Users" -Member $userName
}

Write-Host "Se han configurado los privilegios y restricciones para el usuario '$userName'."