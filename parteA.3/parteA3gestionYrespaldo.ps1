$userName = "RelacionesPublicas"
$desktopPath = "C:\Users\$userName\Desktop"
$comunicadosPath = "$desktopPath\Comunicados"
$semanalPath = "$comunicadosPath\Semanal"
$mensualPath = "$comunicadosPath\Mensual"
$respaldoPath = "C:\Respaldo"
$backupDate = (Get-Date).ToString("ddMMMyyyy").ToUpper()
$backupPath = "$respaldoPath\$backupDate"

# validamos si existen las carpetas o no, sino la creamos
if (-Not (Test-Path -Path $comunicadosPath)) {
    New-Item -ItemType Directory -Path $comunicadosPath
}

if (-Not (Test-Path -Path $semanalPath)) {
    New-Item -ItemType Directory -Path $semanalPath
}

if (-Not (Test-Path -Path $mensualPath)) {
    New-Item -ItemType Directory -Path $mensualPath
}

# creamos la carpeta de respaldo si no existe tambien
if (-Not (Test-Path -Path $respaldoPath)) {
    New-Item -ItemType Directory -Path $respaldoPath
}

# hacemos la carpeta con la fecha de respaldo
New-Item -ItemType Directory -Path $backupPath

# copiamos el contenido de la carpeta Comunicados al respaldo
Copy-Item -Path $comunicadosPath -Destination $backupPath -Recurse

Write-Host "Las carpetas se crearon y el respaldo se hizo exitosamente."
