**Check Defender via PowerShell**

Open PowerShell as administrator:
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
(Once you complete the steps, the real-time antivirus protection will be disabled until the next reboot)
```
Set-MpPreference -DisableRealtimeMonitoring $true

```
