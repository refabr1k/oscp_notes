# Exploits/Tools/Cheatsheets

| **Exploits** | **OS** | **Link** |
| - | - | - |
| CVE-2017-7269 | Windows | [here](../master/IIS6%20CVE-2017-7269) |
| Kernel 2.2.4 PrivEsc (ptrace kmod) | Linux | [here](../master/Kernel_2_2_4_PrivEsc%20(ptrace_kmod)) |
| Kernel 2.6.37 full nelson | Linux | [here](../master/Kernel_2_6_37_fullnelson) |
| MS08-067 Python Reverse Shell | Windows | [here](../master/MS08-067%20Python%20Reverse%20Shell) |
| MS10-015 KiTrap0D | Windows | [here](../master/MS10-015%20KiTrap0D) |
| MS11-046 afd privesc | Windows | [here](../master/MS11-046%20afd%20privesc) |
| MS13-053 NTUserMessageCall | Windows | [here](../master/MS13-053%20NTUserMessageCall) |
| MS14-058 HttpFileServer 2.3 RCE (CVE-2014-6287) | Windows | [here](../master/MS14-058%20HttpFileServer%202.3%20RCE%20(CVE-2014-6287)) |
| MS15-051 ClientCopyImage | Windows | [here](../master/MS15-051%20ClientCopyImage) |
| MS16-032 drivers eop | Windows | [here](../master/MS16-032%20drivers%20eop) |
| MS16-135 win23k | Windows | [here](../master/MS16-135%20win23k) |
| MS17-010 eternalblue | Windows | [here](../master/MS17-010%20eternalblue) |
| Mod SSL 2.8.7 OpenSSL Exploit (openfuckV2.c) | Linux | [here](../master/Mod%20SSL%202.8.7%20OpenSSL%20Exploit%20(openfuckV2.c)) |

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



