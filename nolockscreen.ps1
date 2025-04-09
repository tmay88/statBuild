Clear-Host
Echo "Toggling ScrollLock..."
$WShell = New-Object -com "Wscript.Shell"
while ($true) {
$WShell.sendkeys("{SCROLLLOCK}")
Start-Sleep -milliseconds 200
$WShell.sendkeys("{SCROLLLOCK}")
Start-Sleep -Seconds 90
}