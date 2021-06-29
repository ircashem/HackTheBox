Name & IP Address of Machine:
> BASHED : `10.10.10.68`
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
- [ ] 80 (WEB-SERVER)

## FootHold
A shell is located at `http://10.10.10.68/dev/phpbash.php`

## Lateral Movement
`www-data` can run sudo with scriptmanager permission. 
```bash
sudo -u scriptmanager /bin/bash
```
And we get scriptmanager

## Privilege Escalation

there is a folder `/scripts` where root is running a cron job from test.py or any file inside that directory.
User scriptmanager can edit this file so, we got the flag right away.



<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->