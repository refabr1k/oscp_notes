#!/bin/bash

echo "Running Bash loop to perform a ping sweep of target IP range 10.11.1.0/24"

IP=10.11.1.

for x in `seq 1 254`; do
ping -c 1 $IP$x | grep "64 bytes" | cut -d " " -f 4 | cut -d ":" -f 1
done

echo "Ping sweep complete"

