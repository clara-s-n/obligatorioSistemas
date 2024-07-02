New-LocalUser -Name "RelacionesPublicas" -Password "relacionespublicas" -FullName "Relaciones Publicas" -Description "Usuario de Relaciones Publicas"
Add-LocalGroupMember -Group "Users" -Member "RelacionesPublicas"
Write-Host "El usuario 'RelacionesPublicas' ha sido creado exitosamente."