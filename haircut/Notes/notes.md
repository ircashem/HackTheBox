# haircut : `10.10.10.24`

**Table Of Contents:**

<!-- TOC -->

- [haircut : `10.10.10.24`](#haircut--10101024)
  - [Synopsis](#synopsis)
  - [Enumeration](#enumeration)
    - [Opened Ports](#opened-ports)
  - [FootHold](#foothold)
  - [Lateral Movement](#lateral-movement)
  - [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->

## Synopsis

Command injection on the web server and then screenroot.sh to gain root from www-data to root.

Pretty straightforward. 🚀️

---

## Enumeration

### Opened Ports

- [ ] 22 (SSH)
- [ ] 80 (NGINX)

---

## FootHold

- Had tough time finding exposed.php file on the server via gobuster. Always try medium length wordlist. Don't use shortcut specifically short.txt wordlists. 🗡
- Exposed.php file was on the server. Command injection to get www-data.

---

## Lateral Movement

```bash
-rwsr-xr-x 1 root   root       1.6M May 19  2017 /usr/bin/screen-4.5.0 (Unknown SUID binary)                                         
```

---

## Privilege Escalation

Used screenroot.sh to gain access to root since the screen version 4.5.0 is vulnerable.

---
