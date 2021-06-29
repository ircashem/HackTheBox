Name & IP Address of Machine:
> VALENTINE : `10.10.10.79`
<!-- TOC -->

- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->



## Synopsis
- Run gobuster to get hype_key in hex format
- Decrypt the id_rsa from hex.
- Exploit heartbleed to get the password.
- Running linpeas.sh will reveal a tmux session is in the `/.devs` folder
- User hype has the permision to join the session.
- `tmux -S /tmp/dev_sess ls`


## Enumeration
Opened Ports: 
- [ ] 22 (SSH)
- [ ] 80 (HTTP)
- [ ] 443 (HTTPS)

## FootHold

## Lateral Movement

## Privilege Escalation




<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->