Name & IP Address of Machine:
> NEST : `10.10.10.178`
<!-- TOC -->

- [Synopsis](#synopsis)

<!-- /TOC -->

## Synopsis
- Usernames :
    - C.Smith
    - L.Frost
    - R.Thompson
    - Administrator

- Enumerate Shared smb folder to get creds for TempUser
  `TempUser:welcome2019`
- Now enumerate Data Share and you will get hash for c.smith user.
  ```bash
    cat ./RU\ Scanner/RU_config.xml| grep Pass -B 3
    <ConfigFile xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <Port>389</Port>
    <Username>c.smith</Username>
    <Password>fTEzAfYDoz1YzkqhQkH6GQFYKp1XY5hm7bjOP86yYxE=</Password>
  ```
    `c.smith:fTEzAfYDoz1YzkqhQkH6GQFYKp1XY5hm7bjOP86yYxE=`
- In config file for notepadplusplus, we get to know a directory Carl
  ```bash
    <History nbMaxFile="15" inSubMenu="no" customLength="-1">
        <File filename="C:\windows\System32\drivers\etc\hosts" />
        <File filename="\\HTB-NEST\Secure$\IT\Carl\Temp.txt" />
        <File filename="C:\Users\C.Smith\Desktop\todo.txt" />
    </History
  ```
- Got source code for RUScanner and get to know the encryption mechanism done.
- Decrypt hash to get the password for c.smith
  `c.smith:xRxRxPANCAK3SxRxRx`
- Go into the user's home directory and finds out debug file whose metadata contains password for hvc_service.
- Login to port 4386 using telnet and find administrator password in up directory ldap.conf.
  ```Current Directory: ldap
  >showquery 2

  Domain=nest.local
  Port=389
  BaseOu=OU=WBQ Users,OU=Production,DC=nest,DC=local
  User=Administrator
  Password=yyEq0Uvvhq2uQOcWG8peLoeRQehqip/fKdeG/kjEVb4=
```
## Enumeration
Opened Ports: 
- [ ] .



## FootHold

## Lateral Movement

## Privilege Escalation




<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.

```bash
smbclient -L 10.10.10.178                                                                                                          
Enter WORKGROUP\ircashem's password:                                                                                                   
                                                                                                                                       
        Sharename       Type      Comment                                                                                              
        ---------       ----      -------                                                                                              
        ADMIN$          Disk      Remote Admin                                                                                         
        C$              Disk      Default share                                                                                        
        Data            Disk                                                                                                           
        IPC$            IPC       Remote IPC                                                                                           
        Secure$         Disk                                                                                                           
        Users           Disk                                                                                                           
Reconnecting with SMB1 for workgroup listing.

```
- [ ] . -->