# Exploits/Tools/Cheatsheets

Cheatsheet used for OSCP

| **Exploits** | **OS** | **Link** |
| :--- | :--- | :--- |
| CVE-2017-7269 | Windows | [here](https://github.com/refabr1k/oscp_notes/tree/6043e1c75ffccbcf4d7262867ffdf9ac06a29952/master/IIS6%20CVE-2017-7269/README.md) |
| Kernel 2.2.4 PrivEsc \(ptrace kmod\) | Linux | \[here\]\(../master/Kernel\_2\_2\_4\_PrivEsc%20\(ptrace\_kmod\)\) |
| Kernel 2.6.37 full nelson | Linux | [here](https://github.com/refabr1k/oscp_notes/tree/6043e1c75ffccbcf4d7262867ffdf9ac06a29952/master/Kernel_2_6_37_fullnelson/README.md) |
| MS08-067 Python Reverse Shell | Windows | [here](https://github.com/refabr1k/oscp_notes/tree/6043e1c75ffccbcf4d7262867ffdf9ac06a29952/master/MS08-067%20Python%20Reverse%20Shell/README.md) |
| MS10-015 KiTrap0D | Windows | [here](https://github.com/refabr1k/oscp_notes/tree/6043e1c75ffccbcf4d7262867ffdf9ac06a29952/master/MS10-015%20KiTrap0D/README.md) |
| MS11-046 afd privesc | Windows | [here](https://github.com/refabr1k/oscp_notes/tree/6043e1c75ffccbcf4d7262867ffdf9ac06a29952/master/MS11-046%20afd%20privesc/README.md) |
| MS13-053 NTUserMessageCall | Windows | [here](https://github.com/refabr1k/oscp_notes/tree/6043e1c75ffccbcf4d7262867ffdf9ac06a29952/master/MS13-053%20NTUserMessageCall/README.md) |
| MS14-058 HttpFileServer 2.3 RCE \(CVE-2014-6287\) | Windows | \[here\]\(../master/MS14-058%20HttpFileServer%202.3%20RCE%20\(CVE-2014-6287\)\) |
| MS15-051 ClientCopyImage | Windows | [here](https://github.com/refabr1k/oscp_notes/tree/6043e1c75ffccbcf4d7262867ffdf9ac06a29952/master/MS15-051%20ClientCopyImage/README.md) |
| MS16-032 drivers eop | Windows | [here](https://github.com/refabr1k/oscp_notes/tree/6043e1c75ffccbcf4d7262867ffdf9ac06a29952/master/MS16-032%20drivers%20eop/README.md) |
| MS16-135 win23k | Windows | [here](https://github.com/refabr1k/oscp_notes/tree/6043e1c75ffccbcf4d7262867ffdf9ac06a29952/master/MS16-135%20win23k/README.md) |
| MS17-010 eternalblue | Windows | [here](https://github.com/refabr1k/oscp_notes/tree/6043e1c75ffccbcf4d7262867ffdf9ac06a29952/master/MS17-010%20eternalblue/README.md) |
| Mod SSL 2.8.7 OpenSSL Exploit \(openfuckV2.c\) | Linux | \[here\]\(../master/Mod%20SSL%202.8.7%20OpenSSL%20Exploit%20\(openfuckV2.c\)\) |



## Tools

Onetwopunch - wrapper for unicorn and nmap scan

 source: https://raw.githubusercontent.com/superkojiman/onetwopunch/master/onetwopunch.sh Scan for port using nicornscan \(very fast\) and chain it with nmap vuln nse script scan 1. ping sweep for online hosts into list \`nmap -v -sn 10.11.1-254 -oG all-hosts.txt\` \`grep Up all-hosts.txt &gt; online.hosts.txt\` 2. download onetwopunch script \`wget https://raw.githubusercontent.com/superkojiman/onetwopunch/master/onetwopunch.sh\` 3. run script with nmap -sV option \`./scripts/onetwopunch.sh -t online-hosts.txt -p all -i tap0 -n -sV\` 4. Once complete, navigate to output folder "ndir". Use command to formats all .xml output to html \`for x in $\(ls \*.xml\); do filename=$\(echo $x \| sed 's/xml/html/'\) && xsltproc $x -o $filename; done\` \`wget https://raw.githubusercontent.com/superkojiman/onetwopunch/master/onetwopunch.sh\` \`./scripts/onetwopunch.sh -t online-hosts.txt -p all -i tap0 -n -sV\` 5. Navigate to output folder "ndir" and formats all .xml output to html \`for x in $\(ls \*.xml\); do filename=$\(echo $x \| sed 's/xml/html/'\) && xsltproc $x -o $filename; done\`

Droopescan - drupal scanner

 source: https://github.com/droope/droopescan \`\`\` git clone https://github.com/droope/droopescan.git cd droopescan pip install -r requirements.txt droopescan scan drupal -u http://10.11.1.49 \`\`\`

Samba Checker - checks for samba version

 Checks Samba version as enum4linux messed up? THanks fellow student OS-40285/rewardone \`\`\`bash ./samba\_checker.sh \`\`\`

