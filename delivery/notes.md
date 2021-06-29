Name & IP Address of Machine:
> DELIVERY : `10.10.10.222`
<!-- TOC -->

- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->
- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->



## Synopsis


## Enumeration
Opened Ports: 
- [ ] 22(SSH)
- [ ] 80(HTTP)
- [ ] 8065(MATTERMOST)

- Port 80 has vhost enabled. 
- `helpdesk.delivery.htb` && `delivery.htb`
- `maildeliverer:Youve_G0t_Mail!`
- OSTICKET sql config file
  ```bash
define('DBTYPE','mysql');                                                                                                     
define('DBHOST','localhost');                                                                                                 
define('DBNAME','osticket');                                                                                                  
define('DBUSER','ost_user');                                                                                                  
define('DBPASS','!H3lpD3sk123!');
  ```
- `mmuser:Crack_The_MM_Admin_PW`

`$2a$10$VM6EeymRxJ29r8Wjkr8Dtev0O.1STWb4.4ScG.anuu7v0EFJwgjjO:PleaseSubscribe!21`
$2a$10$VM6EeymRxJ29r8Wjkr8Dtev0O.1STWb4.4ScG.anuu7v0EFJwgjjO:PleaseSubscribe!21

## FootHold

## Lateral Movement

## Privilege Escalation




<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->