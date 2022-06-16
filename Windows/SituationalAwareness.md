**Check PowerShell Logging**

```
reg query HKLM\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging /s

reg query HKLM\SOFTWARE\WOW6432Node\Policies\Microsoft\Windows\PowerShell\Transcription /s
```
**Trace RDP Logins to User Desktops**

Can do a `netstat -ano` which requires CMD/PowerShell

Otherwise:

`Event Viewer > Application and Services Logs > Microsoft > Windows > TerminalServices-LocalSessionManager > Operational`
