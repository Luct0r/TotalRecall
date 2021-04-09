**Check Defender via PowerShell**

Administrator privileges required:
```
Get-MpComputerStatus

Get-MpPreference

```
Exclude file type/locations

```
Set-MpPreference -ExclusionPath PATH\TO\FOLDER

Set-MpPreference -ExclusionExtension EXTENSION
```
Disable antivirus:

(Once you completed, the real-time antivirus protection will be disabled until the next reboot)
```
Set-MpPreference -DisableRealtimeMonitoring $true

```
Roll back definitions:
```
cd "C:\Program Files\Windows Defender\"
MpCMDRun.exe -removedefinitions -all
```
