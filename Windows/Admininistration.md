**Enable RDP**
```
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

netsh advfirewall firewall set rule group="remote desktop" new enable=Yes
```
**Disable RDP**
```
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f

netsh advfirewall firewall set rule group="remote desktop" new enable=No
```
**Rest Firewall**

Open CMD as administrator:
```
netsh advfirewall reset
```
Open PowerShell as administrator:
```
(New-Object -ComObject HNetCfg.FwPolicy2).RestoreLocalFirewallDefaults()
```
