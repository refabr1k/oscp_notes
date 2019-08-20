#!/bin/bash
iptables -Z && iptables -F
iptables -A INPUT -p tcp --destination-port 13327 \! -d 127.0.0.1 -j DROP
iptables -A INPUT -p tcp --destination-port 4444 \! -d 127.0.0.1 -j DROP

