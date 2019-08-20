#!/usr/bin/python

import ipaddress
import os


#ip address string must be in unicode to use ipaddress module
network = ipaddress.ip_network(unicode("10.11.1.0/24"))

print("Running Python ping sweep of target IP range 10.11.1.0/24")

for i in network.hosts():
	#str(i)
	
	response = os.system("ping %s -c 1 > /dev/null" %i)
	
        if response == 0:
                print("%s UP" %i)
        else:
                print("%s No response" %i)

print("Ping sweep complete")
