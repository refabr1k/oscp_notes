#!/bin/bash

for i in `seq 1 99999`; do

	date > iptable_nmap_UDP.log
	iptables -vn -L >> iptable_nmap_UDP.log
	sleep 5m

done
