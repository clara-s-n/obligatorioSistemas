$userName = "Recepcion"
$userProfilePath = "C:\Users\$userName"
$restrictedFolders = "C:\Windows", "C:\Program Files", "C:\Program Files (x86)", "C:\Users\Public"

# prohibimos los accesos a las carpetas
function Deny-Access {
    param (
        [string]$path,
        [string]$userName
    )
    $acl = Get-Acl -Path $path
    $accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("$userName", "FullControl", "Deny")
    $acl.SetAccessRule($accessRule)
    Set-Acl -Path $path -AclObject $acl
}

foreach ($folder in $restrictedFolders) {
    Deny-Access -path $folder -userName $userName
}

# permitimos acceso completo a las carpetas propias del usuario
$userFolders = Get-ChildItem -Path $userProfilePath -Directory
foreach ($folder in $userFolders) {
    $acl = Get-Acl -Path $folder.FullName
    $acl.ResetAccessRuleAll()
    $acl.SetAccessRule((New-Object System.Security.AccessControl.FileSystemAccessRule("$userName", "FullControl", "Allow")))
    Set-Acl -Path $folder.FullName -AclObject $acl
}

Write-Host "Se han configurado las restricciones para el usuario '$userName'."
