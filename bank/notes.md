Name & IP Address of Machine:
> NAME : `<IP>`
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
- [ ] 22 `(SSH)`
- [ ] 53 `(DOMAIN)`
- [ ] 80 `(WEBSERVER)`

## FootHold
On port 80, the default page of apache server is hosted. The port 53 is giving the hint that there is a good possibility that `bank.htb` is available. Adding to this host in our `/etc/hosts` file, we are provided with a login form. Bruterforcing for pages via gobuster reveals a page `support.php` in which the server throws the content of the suppport.php file in addition to a location of `login.php` Since we don't have any authentication yet. Intercepting response of the support.php page and removing the  location header of login.php, we can see `support.php` content.
There is this comment included in the support.php page that the file uploaded as htb extension will be executed as php. So we will try to get a shell from uploading a file `shell.htb`.

## Lateral Movement

```bash
www-data@bank:/var/www/bank$ cat bankreports.txt 
+=================+
| HTB Bank Report |
+=================+

===Users===
Full Name: Christos Christopoulos
Email: chris@bank.htb
Password: !##HTBB4nkP4ssw0rd!##
CreditCards: 2
Transactions: 8
Balance: 1.337$
```
```txt
$mysql = new mysqli("localhost", "root", "!@#S3cur3P4ssw0rd!@#", "htbbank");
```


## Privilege Escalation
```bash
find / -perm -4000 -exec ls -la {} \; # finding suid bit binaries
```
/var/htb/emergency gives us root shell.


<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->