Name & IP Address of Machine:
> HEIST : `10.10.10.149`
<!-- TOC -->

- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->



## Synopsis
- Login to the web server and proceed as guest.
- You will get a config.txt file from which decrypt a hash. 
```bash
 $1$pdQG$o8nrSzsGXeaduXrjlvKc91:stealth1agent
 admin:Q4)sJu\Y8qz*A3?d
 rout3r:$uperP@ssword
```
- rpcclient success
`hazard:stealth1agent`
- Bruteforce for winrm- (Failed)
- But deadend. Try lookup sid from which extract three usernames jason,chase,support.
- Bruteforce again for winrm (Success)
`chase:Q4)sJu\Y8qz*A3?d`
- Todo.txt file reads
  ```txt
    *Evil-WinRM* PS C:\Users\chase\desktop> cat todo.txt
    Stuff to-do:
    1. Keep checking the issues list.
    2. Fix the router config.

    Done:
    1. Restricted access for guest user.
    *Evil-WinRM* PS C:\Users\chase\desktop>
  ```
- Firefox running
  ```bash
   1491      58    23376      78684              2412   1 explorer                                                                     
    355      25    16440      39128       0.14   2704   1 firefox                                                                      
    378      28    22284      59200       0.95   6420   1 firefox                                                                      
   1053      69   147500     223224       9.20   6596   1 firefox                                                                      
    347      19     9904      34224       0.45   6716   1 firefox                                                                      
    401      34    31812      92372       1.48   6884   1 firefox                                                                      
     49       6     1784       4676               776   1 fontdrvhost
     
  ```
- Use procdump to dump firefox process
- Read dump file for any password and you will get:
`4dD!5}x/re8]FBuZ`
- Bruteforce winrm with adding another user Administrator in the user.lst
- `Success`
- 
## Enumeration
Opened Ports: 
- [ ] .



## FootHold

## Lateral Movement

## Privilege Escalation




<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->