Name & IP Address of Machine:
> FRIENDZONE : `10.10.10.123`
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
  - Anonymous access not allowed.
  -  

- [ ] 22 (SSH)
- [ ] 53 (DNS)
  - got domain `friendzone.red`
  - Performed zone transfer `dig axfr friendzone.red @10.10.10.123`
    ```bash
    administrator1.friendzone.red.  604800  IN      A      127.0.0.1
    hr.friendzone.red.              604800  IN      A       127.0.0.1
    uploads.friendzone.red.         604800  IN      A       127.0.0.1
    ```
- [ ] 80 (HTTP WEB SERVER)
- [ ] 139 (SAMBA)
  - `admin:WORKWORKHhallelujah@#` 
- [ ] 443 (HTTPS SERVER)




## FootHold

## Lateral Movement

## Privilege Escalation




<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->