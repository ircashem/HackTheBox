#!/bin/bash

log=/home/ircashem/Desktop/HackTheBox/scriptkiddie/logs/hackers

cd /home/ircashem/
cat /home/ircashem/Desktop/HackTheBox/scriptkiddie/logs/hackers | cut -d' ' -f3- | sort -u | while read ip; do
    # echo "$ip"
    echo "nmap --top-ports 10 -oN recon/${ip}.nmap ${ip} 2>&1 >/dev/null" 
    sh -c "nmap --top-ports 10 -oN recon/${ip}.nmap ${ip} 2>&1 >/dev/null" 
done

# if [[ $(wc -l < $log) -gt 0 ]]; then echo -n > $log; fi