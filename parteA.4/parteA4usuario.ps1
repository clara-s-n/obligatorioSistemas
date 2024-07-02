$securePassword = ConvertTo-SecureString "recepcion" -AsPlainText -Force

New-LocalUser -Name "Recepcion" -Password $securePassword -FullName "Recepcion" -Description "Usuario encargado de la Recepcion"

Add-LocalGroupMember -Group "Users" -Member "Recepcion"

Write-Host "El usuario 'Recepcion' ha sido creado exitosamente."