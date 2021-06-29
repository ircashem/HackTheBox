Name & IP Address of Machine:
> Blocky : `10.10.10.37`
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
- [ ] 21 `(FTP)`
- [ ] 22 `(SSH)`
- [ ] 80 `(Apache Web-Server)`

## FootHold
- Anonymous login for ftp was not allowed however the bannner reaveal `proftpd version 1.3.5a`.
- Did msfconsole and tried to exploit that specific version for ftp but didn't work.
- Moved on to the webserver, wordpress site was hosted.
- Username got: `notch`
- Bruteforcing for directories, came across `plugins`, `phpmyadmin`.
- plugins contains two jar files one on which contains phpmyadmin password of root
- We edit the password of notch from wordpress database and then get a reverse shell from wordpress theme editor.


## Lateral Movement
Password

`phpmyadmin:8YsqfCTnvxAUeduzjNSXe22` ------- `Appears to be notch password` (Reuse password)
`kWuvW2SYsABmzywYRdoD`

## Privilege Escalation
User notch can run sudo to all binary. Since we have his password now.
```bash
sudo /bin/bash
root@Blocky:~# 

```



<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->