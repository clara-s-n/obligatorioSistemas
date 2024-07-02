$scriptPath = "C:\Scripts\MonitorProcesos.ps1"
$taskName = "MonitorarProcesosCPU"

if (-Not (Test-Path -Path "C:\Scripts")) {
    New-Item -ItemType Directory -Path "C:\Scripts"
}

$scriptContent = @"
\$processesPath = "C:\PROCESOS"
\$logFileName = "\$(Get-Date -Format 'yyyyMMdd').txt"
\$logFilePath = "\$processesPath\\$logFileName"
\$userName = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name.Split('\')[-1]

# creamso la carpeta RPOCESOS si no existe
if (-Not (Test-Path -Path \$processesPath)) {
    New-Item -ItemType Directory -Path \$processesPath
}

# agarramso los procesos que consumen mas CPU
\$topProcesses = Get-Process | Sort-Object CPU -Descending | Select-Object -First 10

# lsitado...
\$timeStamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
\$logContent = "\`n[\$timeStamp]\`n" + (\$topProcesses | Format-Table -AutoSize | Out-String)

# guardamos el listado en el archivo
Add-Content -Path \$logFilePath -Value \$logContent

# msotramos el listado solo si el usuario es SOPORTE
if (\$userName -eq "SOPORTE") {
    Write-Host \$logContent
}
"@

Set-Content -Path $scriptPath -Value $scriptContent

if (Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
}

$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File $scriptPath"
$triggerStartup = New-ScheduledTaskTrigger -AtStartup
$triggerRepetition = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 60) -RepetitionDuration (New-TimeSpan -Days 3650)
$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $triggerStartup, $triggerRepetition -Principal $principal

Write-Host "La tarea programada '$taskName' se creo correctamente."