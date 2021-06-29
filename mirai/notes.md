Name & IP Address of Machine:
> MIRAI : `10.10.10.48`
<!-- TOC -->

- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->



## Synopsis


## Enumeration
Opened Ports: 
- [ ] 22 (FTP)
- [ ] 53 (DOMAIN)
- [ ] 80 (WEB-SERVER)
- [ ] 1500 (UPNP)
  
  Doing full port scan reveals another port listening on `32400` which is running a web server.

## FootHold
Pasword reuse of pi-hole `pi:raspberry`

## Lateral Movement

## Privilege Escalation
Run sudo to all binaries .
```bash
sudo /bin/bash
```




<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->