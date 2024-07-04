$contaduriaUserPassword = ConvertTo-SecureString -String "C0NT+" -AsPlainText -Force
New-LocalUser -Name "Contaduria" -Password $contaduriaUserPassword -Description "Usuario del departamento de Contaduria" -AccountNeverExpires:$true

$soporteUserPassword = ConvertTo-SecureString -String "SuPP++" -AsPlainText -Force
New-LocalUser -Name "Soporte" -Password $soporteUserPassword -Description "Usuario encargado del soporte" -AccountNeverExpires:$true

# Agregar usuarios a grupos
Add-LocalGroupMember -Group "Administradores" -Member "Soporte"
Add-LocalGroupMember -Group "Usuarios" -Member "Contaduria"