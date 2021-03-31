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
**Reset Firewall**

Open CMD as administrator:
```
netsh advfirewall reset
```
Open PowerShell as administrator:
```
(New-Object -ComObject HNetCfg.FwPolicy2).RestoreLocalFirewallDefaults()
```
**Windows Firewall ICMP**
```
netsh advFirewall Firewall add rule name="Static page request" protocol=icmpv4:8,any dir=in action=block
```
https://www.windows-commandline.com/add-user-from-command-line/

https://www.top-password.com/blog/add-user-to-remote-desktop-users-group-in-windows-10/

https://doublepulsar.com/rdp-hijacking-how-to-hijack-rds-and-remoteapp-sessions-transparently-to-move-through-an-da2a1e73a5f6

https://www.howtogeek.com/howto/windows-vista/how-to-delete-a-windows-service-in-vista-or-xp/

https://www.windows-commandline.com/start-terminal-services-command-line/

https://www.windows-commandline.com/start-or-stop-workstation-service-from/

https://srvadm.com/command/start-or-stop-workstation-service-from-command-line-cmd/
