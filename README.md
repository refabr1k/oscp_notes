 
**Onetwopunch.sh** (https://raw.githubusercontent.com/superkojiman/onetwopunch/master/onetwopunch.sh) Wrapper for unicornscan (fast port scan) and nmap (vuln script scan)
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