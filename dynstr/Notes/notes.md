Name & IP Address of Machine:
> # dynstr : `10.129.126.206`
**Table Of Contents:**
<!-- TOC -->

- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
    - [Opened Ports:](#opened-ports)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->

## Synopsis
  
- https://www.dynu.com/DynamicDNS/IP-Update-Protocol#responsecode

---

## Enumeration

---
#### Opened Ports: 
- [ ] x

---

## FootHold
`/etc/bind/named.conf.local`
```
zone "0.in-addr.arpa" {
        type master;
        file "/etc/bind/db.0";
};
```
http://dynadns:sndanyd@dyna.htb/nic/update?hostname=ircashem.dyna.htb&myip=10.10.14.15

```bash
echo exploit.sh | /usr/bin/nsupdate -t 1 -k /etc/bind/ddns.key
```

---

## Lateral Movement

---

## Privilege Escalation

---